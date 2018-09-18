import argparse
from lstm import LSTM

_parser = argparse.ArgumentParser(description = "DTT")
_parser.add_argument('--data', type=str, default='./tweets',
                    help='location of the data corpus')
_parser.add_argument('--checkpoint', type=str, default='./model.pt',
                    help='model checkpoint to use')
_parser.add_argument('--outf', type=str, default='generated.txt',
                    help='output file for generated text')
_parser.add_argument('--words', type=int, default='1000',
                    help='number of words to generate')
_parser.add_argument('--seed', type=int, default=1111,
                    help='random seed')
_parser.add_argument('--cuda', action='store_true',
                    help='use CUDA')
_parser.add_argument('--temperature', type=float, default=1.0,
                    help='temperature - higher will increase diversity')
_parser.add_argument('--log-interval', type=int, default=100,
                    help='reporting interval')
_args = _parser.parse_args()

_lstm = LSTM(_args.data, _args.checkpoint, _args.seed, _args.temperature, _args.cuda)

def generate_tweet():
    tweet = list()
    for token in _lstm:
        if token == "<eos>":
            break
        tweet.append(token)
    return " ".join(tweet)