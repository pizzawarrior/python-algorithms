You are given a string binaryString consisting of '0's and '1's, as well as an array of strings requests containing requests of two types:
- requests[i] = "count:<index>" - find the number of '0's in binaryString before and including the specified 0-based index.
- requests[i] = "flip" - flip all elements of binaryString, i.e. change every'0' to '1', and every '1' to '0'.

Return an array answers, where answers[i] contains the answer for the respective count request.

Example:
For binaryString = "1111010" and requests = ["count:4", "count:6", "flip", "count:4", "flip", "count:2"], the output should be solution(binaryString, requests) = [1, 2, 4, 0].

Explanation:
requests[0] = "count:4": the index is 4. Part of the current string before and including the index 4 is binaryString[0-4] = "11110". There is one 0 in it; 1 is appended to the resulting array. It is now equal to [1].
requests[1] = "count:6": the index is 6. Part of the current string before the index 6 is binaryString[0-6] = "1111010". There are two 0s in it; 2 is appended to the resulting array. It is now equal to [1, 2].
requests[2] = "flip": after the flip, the string turns into binaryString = 0000101;
requests[3] = "count:4": the index is 4. Part of the current string before the index 4 is binaryString[0-4] = "00001". There are four 0s in it; 4 is appended to the resulting array. It is now equal to [1, 2, 4].
requests[4] = "flip": after the flip, the string turns into binaryString = 1111010;
requests[6] = "count:2": the index is 2. Part of the current string before the index 2 is binaryString[0-2] = "111". There are zero 0s in it; 0 is appended to the resulting array. It is now equal to [1, 2, 4, 0].

The answers for the count requests are [1, 2, 4, 0].

Input/Output:
[execution time limit] 4 seconds (py3)
[memory limit] 1 GB
[input] string binaryString
A string consisting of '0's and '1's.
Guaranteed constraints:
1 ≤ binaryString.length ≤ 105.
[input] array.string requests
An array of strings representing the requests. It is guaranteed that each requests[i] is either "count:<index>" or "flip".

Guaranteed constraints:
1 ≤ requests.length ≤ 105.
0 ≤ index ≤ binaryString.length - 1.
[output] array.integer

An array answers, where answers[i] is the answer for the respective count request.
