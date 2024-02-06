{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8b7b2224-3fb6-4fde-ac3c-e259b6954281",
   "metadata": {},
   "source": [
    "Solution of 3.8.2, Singh et al. 2015"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "67e36738-d36f-455d-b809-80bac9b21b32",
   "metadata": {},
   "source": [
    "Compute the mean RecombinantFraction for each Drosophila Line and InfectionStatus. Print the results in the following form:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e81bfbb2-c46d-4a38-93dc-80e5d934fc44",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4476f671-a18c-4faf-85f4-422c79fe0a08",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_data = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "950b54bd-1d09-45af-865a-d67a14cce537",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "21 I 0.1826923077\n"
     ]
    }
   ],
   "source": [
    "desktop_path = \"Desktop/Singh2015_data.csv\"\n",
    "with open(desktop_path) as csvfile:\n",
    "    reader = csv.DictReader(csvfile)\n",
    "    for row in reader:\n",
    "        my_line = row['Line']\n",
    "        my_status = row['InfectionStatus']\n",
    "        my_recomb = float(row['RecombinantFraction'])\n",
    "        # Test by printing the values\n",
    "        print(my_line, my_status, my_recomb)\n",
    "        # just print the first row\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3dbb43d0-6ad4-41aa-8bad-c67323cabafe",
   "metadata": {},
   "outputs": [],
   "source": [
    "desktop_path = \"Desktop/Singh2015_data.csv\"\n",
    "with open(desktop_path) as csvfile:\n",
    "    reader = csv.DictReader(csvfile)\n",
    "    for row in reader:\n",
    "        my_line = row['Line']\n",
    "        my_status = row['InfectionStatus']\n",
    "        my_recomb = float(row['RecombinantFraction'])\n",
    "        # if my_line is not present in the dictionary:\n",
    "        if my_line not in my_data:\n",
    "            # create and initialize with a dictionary containing\n",
    "            # two empty lists\n",
    "            my_data[my_line] = {'W': [], 'I': []}\n",
    "        # insert the value in the right list\n",
    "        my_data[my_line][my_status].append(my_recomb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "13fedc88-c2ed-4177-9b35-b3abe1d36c48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'21': {'W': [0.1288343558,\n",
       "   0.163141994,\n",
       "   0.1674208145,\n",
       "   0.1746478873,\n",
       "   0.175,\n",
       "   0.1779661017,\n",
       "   0.191588785,\n",
       "   0.1961722488,\n",
       "   0.2026578073,\n",
       "   0.2032258065,\n",
       "   0.1288343558,\n",
       "   0.163141994,\n",
       "   0.1674208145,\n",
       "   0.1746478873,\n",
       "   0.175,\n",
       "   0.1779661017,\n",
       "   0.191588785,\n",
       "   0.1961722488,\n",
       "   0.2026578073,\n",
       "   0.2032258065],\n",
       "  'I': [0.1826923077,\n",
       "   0.1850393701,\n",
       "   0.1856540084,\n",
       "   0.1866666667,\n",
       "   0.1904761905,\n",
       "   0.1958762887,\n",
       "   0.2180094787,\n",
       "   0.2534246575,\n",
       "   0.1826923077,\n",
       "   0.1850393701,\n",
       "   0.1856540084,\n",
       "   0.1866666667,\n",
       "   0.1904761905,\n",
       "   0.1958762887,\n",
       "   0.2180094787,\n",
       "   0.2534246575]},\n",
       " '40': {'W': [0.125,\n",
       "   0.156424581,\n",
       "   0.1564885496,\n",
       "   0.1595744681,\n",
       "   0.1602209945,\n",
       "   0.1651376147,\n",
       "   0.1694915254,\n",
       "   0.1700404858,\n",
       "   0.1710526316,\n",
       "   0.180952381,\n",
       "   0.1828793774,\n",
       "   0.1888888889,\n",
       "   0.1892857143,\n",
       "   0.2123287671,\n",
       "   0.2247706422,\n",
       "   0.2340425532,\n",
       "   0.125,\n",
       "   0.156424581,\n",
       "   0.1564885496,\n",
       "   0.1595744681,\n",
       "   0.1602209945,\n",
       "   0.1651376147,\n",
       "   0.1694915254,\n",
       "   0.1700404858,\n",
       "   0.1710526316,\n",
       "   0.180952381,\n",
       "   0.1828793774,\n",
       "   0.1888888889,\n",
       "   0.1892857143,\n",
       "   0.2123287671,\n",
       "   0.2247706422,\n",
       "   0.2340425532],\n",
       "  'I': [0.1573426573,\n",
       "   0.1614173228,\n",
       "   0.1666666667,\n",
       "   0.1693989071,\n",
       "   0.1740890688,\n",
       "   0.1779141104,\n",
       "   0.1878980892,\n",
       "   0.2110552764,\n",
       "   0.2153846154,\n",
       "   0.1573426573,\n",
       "   0.1614173228,\n",
       "   0.1666666667,\n",
       "   0.1693989071,\n",
       "   0.1740890688,\n",
       "   0.1779141104,\n",
       "   0.1878980892,\n",
       "   0.2110552764,\n",
       "   0.2153846154]},\n",
       " '45': {'W': [0.1481481481,\n",
       "   0.1625,\n",
       "   0.175862069,\n",
       "   0.1859504132,\n",
       "   0.1906779661,\n",
       "   0.2007722008,\n",
       "   0.2032967033,\n",
       "   0.2033195021,\n",
       "   0.213740458,\n",
       "   0.1481481481,\n",
       "   0.1625,\n",
       "   0.175862069,\n",
       "   0.1859504132,\n",
       "   0.1906779661,\n",
       "   0.2007722008,\n",
       "   0.2032967033,\n",
       "   0.2033195021,\n",
       "   0.213740458],\n",
       "  'I': [0.1666666667,\n",
       "   0.1736111111,\n",
       "   0.1838565022,\n",
       "   0.1862068966,\n",
       "   0.1873015873,\n",
       "   0.1875,\n",
       "   0.188976378,\n",
       "   0.1981707317,\n",
       "   0.1993355482,\n",
       "   0.2068965517,\n",
       "   0.2077922078,\n",
       "   0.2080745342,\n",
       "   0.1666666667,\n",
       "   0.1736111111,\n",
       "   0.1838565022,\n",
       "   0.1862068966,\n",
       "   0.1873015873,\n",
       "   0.1875,\n",
       "   0.188976378,\n",
       "   0.1981707317,\n",
       "   0.1993355482,\n",
       "   0.2068965517,\n",
       "   0.2077922078,\n",
       "   0.2080745342]},\n",
       " '73': {'W': [0.1551724138,\n",
       "   0.1573033708,\n",
       "   0.1653543307,\n",
       "   0.1678321678,\n",
       "   0.1744680851,\n",
       "   0.1802721088,\n",
       "   0.1944444444,\n",
       "   0.1952861953,\n",
       "   0.1956521739,\n",
       "   0.2,\n",
       "   0.1551724138,\n",
       "   0.1573033708,\n",
       "   0.1653543307,\n",
       "   0.1678321678,\n",
       "   0.1744680851,\n",
       "   0.1802721088,\n",
       "   0.1944444444,\n",
       "   0.1952861953,\n",
       "   0.1956521739,\n",
       "   0.2],\n",
       "  'I': [0.1666666667,\n",
       "   0.1812297735,\n",
       "   0.1818181818,\n",
       "   0.1850746269,\n",
       "   0.2109090909,\n",
       "   0.2179487179,\n",
       "   0.2183098592,\n",
       "   0.2339449541,\n",
       "   0.1666666667,\n",
       "   0.1812297735,\n",
       "   0.1818181818,\n",
       "   0.1850746269,\n",
       "   0.2109090909,\n",
       "   0.2179487179,\n",
       "   0.2183098592,\n",
       "   0.2339449541]}}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9e7c181-bd39-4633-bb51-286454c8fa61",
   "metadata": {},
   "outputs": [],
   "source": [
    "Time to calculate the means and print the results:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "42844284-98e4-44c2-a0f0-94423b901e47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Line 21 Average Recombination Rate:\n",
      "W :  0.178\n",
      "I :  0.2\n",
      "\n",
      "Line 40 Average Recombination Rate:\n",
      "W :  0.178\n",
      "I :  0.18\n",
      "\n",
      "Line 45 Average Recombination Rate:\n",
      "W :  0.187\n",
      "I :  0.191\n",
      "\n",
      "Line 73 Average Recombination Rate:\n",
      "W :  0.179\n",
      "I :  0.199\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for line in my_data:\n",
    "    print('Line', line, 'Average Recombination Rate:')\n",
    "    # extract the relevant data\n",
    "    my_subset = my_data[line]\n",
    "    for status in ['W', 'I']:\n",
    "        print(status, ':', end = '') # to prevent new line\n",
    "        my_mean = sum(my_subset[status])\n",
    "        my_num_elements = len(my_subset[status])\n",
    "        my_mean = my_mean / my_num_elements\n",
    "        print(' ', round(my_mean, 3))\n",
    "    print('') # to separate the lines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a470b473-f047-4ca8-89a3-88264d4d6c2d",
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
