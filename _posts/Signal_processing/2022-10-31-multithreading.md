---
layout: post
title:  "Multi-threading and processing on signal processing"
date:   2022-10-31-02T14:28:52-05:00
author: Gyujun Jeong
tags: Research@Agency
---
![alt text]({{ site.baseurl }}/assets/images/general_research/35.PNG "image"){:.profile}<br>


&nbsp;&nbsp;&nbsp;&nbsp;Multithreading and multiprocessing are techniques used to improve the performance of code by allowing multiple tasks to be executed simultaneously.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Multithreading is a technique where multiple threads of execution are created within a single process. Each thread runs independently, allowing multiple tasks to be performed concurrently. In a multithreaded program, each thread shares the same memory space and resources, but each thread has its own stack and set of registers. Multithreading is often used in programs that perform I/O or other blocking operations, where one thread can wait for I/O to complete while another thread performs computation.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Multiprocessing, on the other hand, is a technique where multiple processes are created, each with its own memory space and resources. Each process runs independently, allowing multiple tasks to be performed concurrently. Multiprocessing is often used in programs that perform CPU-intensive tasks, such as image or video processing, where multiple cores or processors can be utilized to improve performance.<br>

&nbsp;&nbsp;&nbsp;&nbsp;The key difference between multithreading and multiprocessing is that multithreading allows multiple threads to execute within the same process, while multiprocessing allows multiple processes to execute concurrently.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Both techniques can improve code performance by leveraging the power of modern CPUs, which typically have multiple cores or processors. By dividing tasks among multiple threads or processes, the workload can be distributed across multiple cores or processors, resulting in faster execution times. However, the choice of whether to use multithreading or multiprocessing depends on the nature of the task being performed and the resources available. In general, multithreading is preferred for tasks that involve I/O or other blocking operations, while multiprocessing is preferred for tasks that are CPU-intensive.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Suppose we need to read and process a signal file that has a large data size. Reading and processing the signal would take a significant amount of time. To improve the performance, we can use multithreading for the signal readout sequence and multiprocessing for the signal processing sequence. Here is the code for the signal readout and processing, including fixed-point conversion:<br>
<script src="https://gist.github.com/gyulab/c5c47615111e88463c299d5658c6a8c2.js"></script>

&nbsp;&nbsp;&nbsp;&nbsp;Since reading the file is an I/O bound operation, let's apply multithreading to the readout part now:<br>
<script src="https://gist.github.com/gyulab/5e15514c95a655bc9c5acf5869af99a6.js"></script><br>
&nbsp;&nbsp;&nbsp;&nbsp;To implement multithreading for the readoutSignal function, we can split the input file into multiple parts and read each part in a separate thread. In this implementation, the num_threads parameter specifies the number of threads to use. The file_size variable is calculated using the os.path.getsize function, and the chunk_size is calculated based on the file size and the number of threads. The chunks variable is a list of file positions, each representing the start of a chunk.

&nbsp;&nbsp;&nbsp;&nbsp;We create a thread for each chunk using the threading.Thread constructor and pass the read_chunk function as the target. The args parameter is used to pass the start and end file positions to the function. We start each thread with the start() method. After starting all threads, we wait for them to complete using the join() method. Once all threads have completed, we concatenate all the results in the results list and return the final read input data as a single array.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Now, let's apply multiprocessing to the signal processing part, specifically the fixed-point conversion, since file processing is a CPU-bound operation:<br>
<script src="https://gist.github.com/gyulab/d6922040bb027142a2c5825572d3b8b7.js"></script><br>
&nbsp;&nbsp;&nbsp;&nbsp;This code defines a function called <code>multiprocessFixedtoFloat</code> that takes in an <code>input_data</code> array as an argument. The goal of this function is to convert the fixed-point numbers in <code>input_data</code> to floating-point numbers using multiple processes to speed up the computation. The first line of the function uses the <code>multiprocessing.cpu_count()</code> function to get the number of available CPUs on the system, and then subtracts 1 to leave one CPU available for other tasks. This value is stored in the num_cpu variable. Each chunk is created by slicing the input_data array into a piece of length <code>pool_length</code>. The chunks are stored in the <code>chunks</code> list. The <code>multiprocessing.Pool()</code> function is then used to create a pool of worker processes, with the number of processes equal to num_cpu. The <code>pool.map()</code> function is used to apply the convertFixedPoint function to each chunk of input_data in parallel. The <code>pool_results</code> variable is assigned the result of the <code>pool.map()</code> function, which is a list of arrays of floating-point numbers. The <code>pool.close()</code> function is then called to close the pool of worker processes.

<br><br>

<b>[References]</b>
1. https://levelup.gitconnected.com/multi-threading-and-multiprocessing-in-python-3d5662f4a528
