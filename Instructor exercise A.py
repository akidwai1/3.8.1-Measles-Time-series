{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5c6e95c5-d71e-423d-af64-0be86764393c",
   "metadata": {},
   "source": [
    "3. Instructor exercise A (output from population simulator):"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f04c94c-7fc5-4b45-9229-93ab76f0d811",
   "metadata": {},
   "source": [
    "a. Edit your population genetics simulator to output the allele frequency of A for each generation, so that you could produce a graph like those in slide 16 from today's powerpoint.  First, simply print this information to screen. Next, save the allele frequencies in a list and output them as a .csv file. Run the code with A = 0.5 starting frequency and N = 10 (pop) and N = 100 population sizes."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d66b3b1-00f2-4ea8-9fd4-9cac5634226a",
   "metadata": {},
   "source": [
    "b. Submit your code as a .py file and your output files as a .csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e3e0da5f-6813-401f-a5b6-b4802df00cb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Population size: 10, Generation: 1, Allele frequency of A: 0.3\n",
      "Population size: 10, Generation: 2, Allele frequency of A: 0.5\n",
      "Population size: 10, Generation: 3, Allele frequency of A: 0.5\n",
      "Population size: 10, Generation: 4, Allele frequency of A: 0.5\n",
      "Population size: 10, Generation: 5, Allele frequency of A: 0.6\n",
      "Population size: 10, Generation: 6, Allele frequency of A: 0.6\n",
      "Population size: 10, Generation: 7, Allele frequency of A: 0.4\n",
      "Population size: 10, Generation: 8, Allele frequency of A: 0.5\n",
      "Population size: 10, Generation: 9, Allele frequency of A: 0.3\n",
      "Population size: 10, Generation: 10, Allele frequency of A: 0.6\n",
      "Population size: 100, Generation: 1, Allele frequency of A: 0.42\n",
      "Population size: 100, Generation: 2, Allele frequency of A: 0.54\n",
      "Population size: 100, Generation: 3, Allele frequency of A: 0.57\n",
      "Population size: 100, Generation: 4, Allele frequency of A: 0.51\n",
      "Population size: 100, Generation: 5, Allele frequency of A: 0.57\n",
      "Population size: 100, Generation: 6, Allele frequency of A: 0.53\n",
      "Population size: 100, Generation: 7, Allele frequency of A: 0.55\n",
      "Population size: 100, Generation: 8, Allele frequency of A: 0.56\n",
      "Population size: 100, Generation: 9, Allele frequency of A: 0.54\n",
      "Population size: 100, Generation: 10, Allele frequency of A: 0.45\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import csv\n",
    "\n",
    "# Function to simulate a single generation of population genetics\n",
    "def simulate_generation(A, N):\n",
    "    # Create a population with given initial allele frequency\n",
    "    population = ['A' if random.random() < A else 'a' for _ in range(N)]\n",
    "    \n",
    "    # Calculate the allele frequency of A in the population\n",
    "    freq_A = population.count('A') / N\n",
    "    \n",
    "    return freq_A\n",
    "\n",
    "# Initialize parameters\n",
    "A = 0.5\n",
    "population_sizes = [10, 100]\n",
    "\n",
    "# Output allele frequencies to screen and save to CSV file\n",
    "for N in population_sizes:\n",
    "    allele_frequencies = []\n",
    "    for _ in range(10):  # 10 generations\n",
    "        freq_A = simulate_generation(A, N)\n",
    "        allele_frequencies.append(freq_A)\n",
    "        \n",
    "        # Output allele frequency to screen\n",
    "        print(f\"Population size: {N}, Generation: {_+1}, Allele frequency of A: {freq_A}\")\n",
    "    \n",
    "    # Save allele frequencies to a CSV file\n",
    "    with open(f'allele_frequencies_N{N}.csv', 'w', newline='') as csvfile:\n",
    "        writer = csv.writer(csvfile)\n",
    "        writer.writerow(allele_frequencies)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a00783f0-5fba-4a9e-a3f3-2de77f661cd3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
