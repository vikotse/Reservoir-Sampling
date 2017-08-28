import random
import sys

def reservoir_sampling(sampled_num, total_num):
    pool = []
    for i in range(0, total_num):
        if i < sampled_num:
            pool.append(i)
        else:
            r = random.randint(0, i)
            if r < sampled_num:
                pool[r] = i
    return pool

def main():
    # sys.argv: <run.py, in_file_path, out_file_path, sampled_num>
    if len(sys.argv) != 4:
        sys.exit(-1)

    in_file_path = sys.argv[1]
    out_file_path = sys.argv[2]
    sampled_num = int(sys.argv[3])

    with open(in_file_path, 'r') as in_file:
        num_lines = sum(1 for line in in_file)

    if num_lines <= sampled_num:
        with open(in_file_path, 'r') as in_file, open(out_file_path, 'w') as out_file:
            for line in in_file:
                out_file.write(line)
    else:
        sampled_indices = reservoir_sampling(sampled_num, num_lines)
        sampled_indices = set(sampled_indices)

        with open(in_file_path, 'r') as in_file, open(out_file_path, 'w') as out_file:
            sampled_counter = 0
            line_counter = 0
            for line in in_file:
                if sampled_counter >= sampled_num:
                    break

                if line_counter in sampled_indices:
                    out_file.write(line)
                    sampled_counter += 1

                line_counter += 1

if __name__ == '__main__':
    main()