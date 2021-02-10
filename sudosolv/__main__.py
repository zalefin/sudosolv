from argparse import ArgumentParser
import sudosolv


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("PATH", help="Path to state file")
    args = parser.parse_args()
    with open(args.PATH, 'r') as f:
        state = sudosolv.string2state(f.read())
        sudosolv.run_solver(state, verbose=True)

