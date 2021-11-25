import argparse
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode')
    parser.add_argument('--input')
    args = parser.parse_args()

    if args.mode == 'encode':
        shift = input('Enter cipher: ')
        shift = int(shift)
        text = np.array(bytearray(args.input, 'utf-8'))
        encoding = text + shift
        encoding = bytearray(encoding).decode()
        print(encoding)
    elif args.mode == 'decode':
        shift = input('Enter cipher: ')
        shift = int(shift)
        text = np.array(bytearray(args.input, 'utf-8'))
        decoding = text - shift
        decoding = bytearray(decoding).decode()
        print(decoding)
    else:
        print("Invalid mode")
