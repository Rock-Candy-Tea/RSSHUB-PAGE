
---
title: '十大经典排序算法动画解析和 Java 代码实现'
categories: 
 - 编程
 - 码农网
 - 最新
headimg: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/011.png'
author: 码农网
comments: false
date: Wed, 09 Jan 2019 11:50:04 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/011.png'
---

<div>   
<p><strong>排序算法是《数据结构与算法》中最基本的算法之一。</strong></p>
<p>排序算法可以分为<strong>内部排序</strong>和<strong>外部排序</strong>。</p>
<p>内部排序是数据记录在内存中进行排序。</p>
<p>而外部排序是因排序的数据很大，一次不能容纳全部的排序记录，在排序过程中需要访问外存。</p>
<p>常见的内部排序算法有：插入排序、希尔排序、选择排序、冒泡排序、归并排序、快速排序、堆排序、基数排序等。</p>
<p>用一张图概括：</p>
<p><img class="aligncenter size-full wp-image-56938" title="01" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/011.png" alt width="966" height="588" referrerpolicy="no-referrer"></p>
<p id="h"><strong>关于时间复杂度：</strong></p>
<ol>
<li>平方阶 (O(n2)) 排序 各类简单排序：直接插入、直接选择和冒泡排序。</li>
<li>线性对数阶 (O(nlog2n)) 排序 快速排序、堆排序和归并排序；</li>
<li>O(n1+§)) 排序，§ 是介于 0 和 1 之间的常数。 希尔排序</li>
<li>线性阶 (O(n)) 排序 基数排序，此外还有桶、箱排序。</li>
</ol>
<p id="h-1"><strong>关于稳定性：</strong></p>
<ol>
<li>稳定的排序算法：冒泡排序、插入排序、归并排序和基数排序。</li>
<li>不是稳定的排序算法：选择排序、快速排序、希尔排序、堆排序。</li>
</ol>
<h2 id="h1">1. 冒泡排序</h2>
<h3 id="h11">1.1 算法步骤</h3>
<ul>
<li>比较相邻的元素。如果第一个比第二个大，就交换他们两个。</li>
<li>对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。</li>
<li>针对所有的元素重复以上的步骤，除了最后一个。</li>
<li>持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。</li>
</ul>
<h3 id="h12">1.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56939" title="1940317-fafcf49997d511ee" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-fafcf49997d511ee.gif" alt width="954" height="537" referrerpolicy="no-referrer"></p>
<h3 id="h13">1.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1// Java 代码实现
 2public class BubbleSort implements IArraySort &#123;
 3
 4    @Override
 5    public int[] sort(int[] sourceArray) throws Exception &#123;
 6        // 对 arr 进行拷贝，不改变参数内容
 7        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 8
 9        for (int i = 1; i < arr.length; i++) &#123;
10            // 设定一个标记，若为true，则表示此次循环没有进行交换，也就是待排序列已经有序，排序已经完成。
11            boolean flag = true;
12
13            for (int j = 0; j < arr.length - i; j++) &#123;
14                if (arr[j] > arr[j + 1]) &#123;
15                    int tmp = arr[j];
16                    arr[j] = arr[j + 1];
17                    arr[j + 1] = tmp;
18
19                    flag = false;
20                &#125;
21            &#125;
22
23            if (flag) &#123;
24                break;
25            &#125;
26        &#125;
27        return arr;
28    &#125;
29&#125;</pre>
<h2 id="h2">2. 选择排序</h2>
<h3 id="h21">2.1 算法步骤</h3>
<ul>
<li>首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置</li>
<li>再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。</li>
<li>重复第二步，直到所有元素均排序完毕。</li>
</ul>
<h3 id="h22">2.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56940" title="1940317-b69f69ee21073f80" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-b69f69ee21073f80.gif" alt width="954" height="537" referrerpolicy="no-referrer"></p>
<h3 id="h23">2.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1//Java 代码实现
 2public class SelectionSort implements IArraySort &#123;
 3
 4    @Override
 5    public int[] sort(int[] sourceArray) throws Exception &#123;
 6        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 7
 8        // 总共要经过 N-1 轮比较
 9        for (int i = 0; i < arr.length - 1; i++) &#123;
10            int min = i;
11
12            // 每轮需要比较的次数 N-i
13            for (int j = i + 1; j < arr.length; j++) &#123;
14                if (arr[j] < arr[min]) &#123;
15                    // 记录目前能找到的最小值元素的下标
16                    min = j;
17                &#125;
18            &#125;
19
20            // 将找到的最小值和i位置所在的值进行交换
21            if (i != min) &#123;
22                int tmp = arr[i];
23                arr[i] = arr[min];
24                arr[min] = tmp;
25            &#125;
26
27        &#125;
28        return arr;
29    &#125;
30&#125;</pre>
<h2 id="h3">3. 插入排序</h2>
<h3 id="h31">3.1 算法步骤</h3>
<ul>
<li>将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。</li>
<li>从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）</li>
</ul>
<h3 id="h32">3.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56941" title="1940317-9455ff13bc8fbdc6" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-9455ff13bc8fbdc6.gif" alt width="955" height="538" referrerpolicy="no-referrer"></p>
<h3 id="h33">3.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1//Java 代码实现
 2public class InsertSort implements IArraySort &#123;
 3
 4    @Override
 5    public int[] sort(int[] sourceArray) throws Exception &#123;
 6        // 对 arr 进行拷贝，不改变参数内容
 7        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 8
 9        // 从下标为1的元素开始选择合适的位置插入，因为下标为0的只有一个元素，默认是有序的
10        for (int i = 1; i < arr.length; i++) &#123;
11
12            // 记录要插入的数据
13            int tmp = arr[i];
14
15            // 从已经排序的序列最右边的开始比较，找到比其小的数
16            int j = i;
17            while (j > 0 && tmp < arr[j - 1]) &#123;
18                arr[j] = arr[j - 1];
19                j--;
20            &#125;
21
22            // 存在比其小的数，插入
23            if (j != i) &#123;
24                arr[j] = tmp;
25            &#125;
26
27        &#125;
28        return arr;
29    &#125;
30&#125;</pre>
<h2 id="h4">4. 希尔排序</h2>
<h3 id="h41">4.1 算法步骤</h3>
<ul>
<li>选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；</li>
<li>按增量序列个数 k，对序列进行 k 趟排序；</li>
<li>每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。</li>
</ul>
<h3 id="h42">4.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56942" title="1940317-acc6c6f16b096794" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-acc6c6f16b096794.gif" alt width="954" height="537" referrerpolicy="no-referrer"></p>
<h3 id="h43">4.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1//Java 代码实现
 2public class ShellSort implements IArraySort &#123;
 3
 4    @Override
 5    public int[] sort(int[] sourceArray) throws Exception &#123;
 6        // 对 arr 进行拷贝，不改变参数内容
 7        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 8
 9        int gap = 1;
10        while (gap < arr.length) &#123;
11            gap = gap * 3 + 1;
12        &#125;
13
14        while (gap > 0) &#123;
15            for (int i = gap; i < arr.length; i++) &#123;
16                int tmp = arr[i];
17                int j = i - gap;
18                while (j >= 0 && arr[j] > tmp) &#123;
19                    arr[j + gap] = arr[j];
20                    j -= gap;
21                &#125;
22                arr[j + gap] = tmp;
23            &#125;
24            gap = (int) Math.floor(gap / 3);
25        &#125;
26
27        return arr;
28    &#125;
29&#125;</pre>
<h2 id="h5">5. 归并排序</h2>
<h3 id="h51">5.1 算法步骤</h3>
<ul>
<li>申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；</li>
<li>设定两个指针，最初位置分别为两个已经排序序列的起始位置；</li>
<li>比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；</li>
<li>重复步骤 3 直到某一指针达到序列尾；</li>
<li>将另一序列剩下的所有元素直接复制到合并序列尾。</li>
</ul>
<h3 id="h52">5.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56943" title="1940317-d3d400686bc61c30" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-d3d400686bc61c30.gif" alt width="954" height="537" referrerpolicy="no-referrer"></p>
<h3 id="h53">5.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1public class MergeSort implements IArraySort &#123;
 2
 3    @Override
 4    public int[] sort(int[] sourceArray) throws Exception &#123;
 5        // 对 arr 进行拷贝，不改变参数内容
 6        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 7
 8        if (arr.length < 2) &#123;
 9            return arr;
10        &#125;
11        int middle = (int) Math.floor(arr.length / 2);
12
13        int[] left = Arrays.copyOfRange(arr, 0, middle);
14        int[] right = Arrays.copyOfRange(arr, middle, arr.length);
15
16        return merge(sort(left), sort(right));
17    &#125;
18
19    protected int[] merge(int[] left, int[] right) &#123;
20        int[] result = new int[left.length + right.length];
21        int i = 0;
22        while (left.length > 0 && right.length > 0) &#123;
23            if (left[0] <= right[0]) &#123;
24                result[i++] = left[0];
25                left = Arrays.copyOfRange(left, 1, left.length);
26            &#125; else &#123;
27                result[i++] = right[0];
28                right = Arrays.copyOfRange(right, 1, right.length);
29            &#125;
30        &#125;
31
32        while (left.length > 0) &#123;
33            result[i++] = left[0];
34            left = Arrays.copyOfRange(left, 1, left.length);
35        &#125;
36
37        while (right.length > 0) &#123;
38            result[i++] = right[0];
39            right = Arrays.copyOfRange(right, 1, right.length);
40        &#125;
41
42        return result;
43    &#125;
44
45&#125;</pre>
<h2 id="h6">6. 快速排序</h2>
<h3 id="h61">6.1 算法步骤</h3>
<ul>
<li>从数列中挑出一个元素，称为 “基准”（pivot）;</li>
<li>重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；</li>
<li>递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；</li>
</ul>
<h3 id="h62">6.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56944" title="1940317-6d01faf07a21e730" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-6d01faf07a21e730.gif" alt width="954" height="537" referrerpolicy="no-referrer"></p>
<h3 id="h63">6.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1//Java 代码实现
 2public class QuickSort implements IArraySort &#123;
 3
 4    @Override
 5    public int[] sort(int[] sourceArray) throws Exception &#123;
 6        // 对 arr 进行拷贝，不改变参数内容
 7        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 8
 9        return quickSort(arr, 0, arr.length - 1);
10    &#125;
11
12    private int[] quickSort(int[] arr, int left, int right) &#123;
13        if (left < right) &#123;
14            int partitionIndex = partition(arr, left, right);
15            quickSort(arr, left, partitionIndex - 1);
16            quickSort(arr, partitionIndex + 1, right);
17        &#125;
18        return arr;
19    &#125;
20
21    private int partition(int[] arr, int left, int right) &#123;
22        // 设定基准值（pivot）
23        int pivot = left;
24        int index = pivot + 1;
25        for (int i = index; i <= right; i++) &#123;
26            if (arr[i] < arr[pivot]) &#123;
27                swap(arr, i, index);
28                index++;
29            &#125;
30        &#125;
31        swap(arr, pivot, index - 1);
32        return index - 1;
33    &#125;
34
35    private void swap(int[] arr, int i, int j) &#123;
36        int temp = arr[i];
37        arr[i] = arr[j];
38        arr[j] = temp;
39    &#125;
40
41&#125;</pre>
<h2 id="h7">7. 堆排序</h2>
<h3 id="h71">7.1 算法步骤</h3>
<ul>
<li>创建一个堆 H[0……n-1]；</li>
<li>把堆首（最大值）和堆尾互换；</li>
<li>把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；</li>
<li>重复步骤 2，直到堆的尺寸为 1。</li>
</ul>
<h3 id="h72">7.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56945" title="1940317-047a907d162a4a0b" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-047a907d162a4a0b.gif" alt width="954" height="537" referrerpolicy="no-referrer"></p>
<h3 id="h73">7.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1//Java 代码实现
 2public class HeapSort implements IArraySort &#123;
 3
 4    @Override
 5    public int[] sort(int[] sourceArray) throws Exception &#123;
 6        // 对 arr 进行拷贝，不改变参数内容
 7        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 8
 9        int len = arr.length;
10
11        buildMaxHeap(arr, len);
12
13        for (int i = len - 1; i > 0; i--) &#123;
14            swap(arr, 0, i);
15            len--;
16            heapify(arr, 0, len);
17        &#125;
18        return arr;
19    &#125;
20
21    private void buildMaxHeap(int[] arr, int len) &#123;
22        for (int i = (int) Math.floor(len / 2); i >= 0; i--) &#123;
23            heapify(arr, i, len);
24        &#125;
25    &#125;
26
27    private void heapify(int[] arr, int i, int len) &#123;
28        int left = 2 * i + 1;
29        int right = 2 * i + 2;
30        int largest = i;
31
32        if (left < len && arr[left] > arr[largest]) &#123;
33            largest = left;
34        &#125;
35
36        if (right < len && arr[right] > arr[largest]) &#123;
37            largest = right;
38        &#125;
39
40        if (largest != i) &#123;
41            swap(arr, i, largest);
42            heapify(arr, largest, len);
43        &#125;
44    &#125;
45
46    private void swap(int[] arr, int i, int j) &#123;
47        int temp = arr[i];
48        arr[i] = arr[j];
49        arr[j] = temp;
50    &#125;
51
52&#125;</pre>
<h2 id="h8">8. 计数排序</h2>
<h3 id="h81">8.1 算法步骤</h3>
<ul>
<li>花O(n)的时间扫描一下整个序列 A，获取最小值 min 和最大值 max</li>
<li>开辟一块新的空间创建新的数组 B，长度为 ( max – min + 1)</li>
<li>数组 B 中 index 的元素记录的值是 A 中某元素出现的次数</li>
<li>最后输出目标整数序列，具体的逻辑是遍历数组 B，输出相应元素以及对应的个数</li>
</ul>
<h3 id="h82">8.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56946" title="1940317-ea11a52dedaf0795" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-ea11a52dedaf0795.gif" alt width="954" height="537" referrerpolicy="no-referrer"></p>
<h3 id="h83">8.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1//Java 代码实现
 2public class CountingSort implements IArraySort &#123;
 3
 4    @Override
 5    public int[] sort(int[] sourceArray) throws Exception &#123;
 6        // 对 arr 进行拷贝，不改变参数内容
 7        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 8
 9        int maxValue = getMaxValue(arr);
10
11        return countingSort(arr, maxValue);
12    &#125;
13
14    private int[] countingSort(int[] arr, int maxValue) &#123;
15        int bucketLen = maxValue + 1;
16        int[] bucket = new int[bucketLen];
17
18        for (int value : arr) &#123;
19            bucket[value]++;
20        &#125;
21
22        int sortedIndex = 0;
23        for (int j = 0; j < bucketLen; j++) &#123;
24            while (bucket[j] > 0) &#123;
25                arr[sortedIndex++] = j;
26                bucket[j]--;
27            &#125;
28        &#125;
29        return arr;
30    &#125;
31
32    private int getMaxValue(int[] arr) &#123;
33        int maxValue = arr[0];
34        for (int value : arr) &#123;
35            if (maxValue < value) &#123;
36                maxValue = value;
37            &#125;
38        &#125;
39        return maxValue;
40    &#125;
41
42&#125;. 桶排序</pre>
<h3 id="h91">9.1 算法步骤</h3>
<ul>
<li>设置固定数量的空桶。</li>
<li>把数据放到对应的桶中。</li>
<li>对每个不为空的桶中数据进行排序。</li>
<li>拼接不为空的桶中数据，得到结果</li>
</ul>
<h3 id="h92">9.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56947" title="20190107115253" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/20190107115253.gif" alt width="955" height="539" referrerpolicy="no-referrer"></p>
<h3 id="h93">9.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1//Java 代码实现
 2public class BucketSort implements IArraySort &#123;
 3
 4    private static final InsertSort insertSort = new InsertSort();
 5
 6    @Override
 7    public int[] sort(int[] sourceArray) throws Exception &#123;
 8        // 对 arr 进行拷贝，不改变参数内容
 9        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
10
11        return bucketSort(arr, 5);
12    &#125;
13
14    private int[] bucketSort(int[] arr, int bucketSize) throws Exception &#123;
15        if (arr.length == 0) &#123;
16            return arr;
17        &#125;
18
19        int minValue = arr[0];
20        int maxValue = arr[0];
21        for (int value : arr) &#123;
22            if (value < minValue) &#123;
23                minValue = value;
24            &#125; else if (value > maxValue) &#123;
25                maxValue = value;
26            &#125;
27        &#125;
28
29        int bucketCount = (int) Math.floor((maxValue - minValue) / bucketSize) + 1;
30        int[][] buckets = new int[bucketCount][0];
31
32        // 利用映射函数将数据分配到各个桶中
33        for (int i = 0; i < arr.length; i++) &#123;
34            int index = (int) Math.floor((arr[i] - minValue) / bucketSize);
35            buckets[index] = arrAppend(buckets[index], arr[i]);
36        &#125;
37
38        int arrIndex = 0;
39        for (int[] bucket : buckets) &#123;
40            if (bucket.length <= 0) &#123;
41                continue;
42            &#125;
43            // 对每个桶进行排序，这里使用了插入排序
44            bucket = insertSort.sort(bucket);
45            for (int value : bucket) &#123;
46                arr[arrIndex++] = value;
47            &#125;
48        &#125;
49
50        return arr;
51    &#125;
52
53    /**
54     * 自动扩容，并保存数据
55     *
56     * @param arr
57     * @param value
58     */
59    private int[] arrAppend(int[] arr, int value) &#123;
60        arr = Arrays.copyOf(arr, arr.length + 1);
61        arr[arr.length - 1] = value;
62        return arr;
63    &#125;
64
65&#125;</pre>
<h2 id="h10">10. 基数排序</h2>
<h3 id="h101">10.1 算法步骤</h3>
<ul>
<li>将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零</li>
<li>从最低位开始，依次进行一次排序</li>
<li>从最低位排序一直到最高位排序完成以后, 数列就变成一个有序序列</li>
</ul>
<h3 id="h102">10.2 动画演示</h3>
<p><img class="aligncenter size-full wp-image-56948" title="1940317-f795324456e5717d" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/01/1940317-f795324456e5717d.gif" alt width="954" height="537" referrerpolicy="no-referrer"></p>
<h3 id="h103">10.3 参考代码</h3>
<pre class="brush: java; gutter: true; first-line: 1"> 1//Java 代码实现
 2public class RadixSort implements IArraySort &#123;
 3
 4    @Override
 5    public int[] sort(int[] sourceArray) throws Exception &#123;
 6        // 对 arr 进行拷贝，不改变参数内容
 7        int[] arr = Arrays.copyOf(sourceArray, sourceArray.length);
 8
 9        int maxDigit = getMaxDigit(arr);
10        return radixSort(arr, maxDigit);
11    &#125;
12
13    /**
14     * 获取最高位数
15     */
16    private int getMaxDigit(int[] arr) &#123;
17        int maxValue = getMaxValue(arr);
18        return getNumLenght(maxValue);
19    &#125;
20
21    private int getMaxValue(int[] arr) &#123;
22        int maxValue = arr[0];
23        for (int value : arr) &#123;
24            if (maxValue < value) &#123;
25                maxValue = value;
26            &#125;
27        &#125;
28        return maxValue;
29    &#125;
30
31    protected int getNumLenght(long num) &#123;
32        if (num == 0) &#123;
33            return 1;
34        &#125;
35        int lenght = 0;
36        for (long temp = num; temp != 0; temp /= 10) &#123;
37            lenght++;
38        &#125;
39        return lenght;
40    &#125;
41
42    private int[] radixSort(int[] arr, int maxDigit) &#123;
43        int mod = 10;
44        int dev = 1;
45
46        for (int i = 0; i < maxDigit; i++, dev *= 10, mod *= 10) &#123;
47            // 考虑负数的情况，这里扩展一倍队列数，其中 [0-9]对应负数，[10-19]对应正数 (bucket + 10)
48            int[][] counter = new int[mod * 2][0];
49
50            for (int j = 0; j < arr.length; j++) &#123;
51                int bucket = ((arr[j] % mod) / dev) + mod;
52                counter[bucket] = arrayAppend(counter[bucket], arr[j]);
53            &#125;
54
55            int pos = 0;
56            for (int[] bucket : counter) &#123;
57                for (int value : bucket) &#123;
58                    arr[pos++] = value;
59                &#125;
60            &#125;
61        &#125;
62
63        return arr;
64    &#125;
65    private int[] arrayAppend(int[] arr, int value) &#123;
66        arr = Arrays.copyOf(arr, arr.length + 1);
67        arr[arr.length - 1] = value;
68        return arr;
69    &#125;
70&#125;</pre>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            