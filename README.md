# Python vs C MPI Performance Comparison

## Project Spec
> "I would make a recommendation of comparing at least 3 different MPI algorithms performance in C/C++ vs the same algorithm in Python or Rust as your primary inquiry question. Opt for a dockerized comparison as an add-on if you have time. I’ve gotten MPI running in K8s and it was far from trivial and that was ignoring the testing, algorithms, etc that I would want you to write to test the performance differences."

### Testing methodology

For each of the 3 algorithms, test input sizes of 1000, 10000, and 100000 for 5 runs and average the runtimes. 