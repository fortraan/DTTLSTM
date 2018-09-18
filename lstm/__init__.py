import torch
from lstm.data import Corpus

class LSTM:
    def __init__(self, data, checkpoint, seed = 1000, temperature = 1, use_cuda = False):
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            if not use_cuda:
                print("BTW you can use cuda. Add --cuda to the command to enable it.")
        self._device = torch.device("cuda" if use_cuda else "cpu")
        if temperature < 1e-3:
            raise Exception("Temperature must be > 1e-3")
        self._temperature = temperature
        with open(checkpoint, 'rb') as f:
            self._model = torch.load(f).to(self._device)
        self._model.eval()
        self._corpus = Corpus(data)
        self._ntokens = len(self._corpus.dictionary)
        self._hidden = self._model.init_hidden(1)
        self._input = torch.randint(self._ntokens, (1, 1), dtype = torch.long).to(self._device)

    def __iter__(self):
        return self

    def __next__(self):
        with torch.no_grad():
            output, self._hidden = self._model(self._input, self._hidden)
            word_weights = output.squeeze().div(self._temperature).exp().cpu()
            word_idx = torch.multinomial(word_weights, 1)[0]
            self._input.fill_(word_idx)
            return self._corpus.dictionary.idx2word[word_idx]