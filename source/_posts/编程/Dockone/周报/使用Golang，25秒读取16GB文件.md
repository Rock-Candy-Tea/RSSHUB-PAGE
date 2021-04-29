
---
title: '使用Golang，25秒读取16GB文件'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=489'
author: Dockone
comments: false
date: 2021-04-29 08:02:30
thumbnail: 'https://picsum.photos/400/300?random=489'
---

<div>   
<br>当今世界的任何计算机系统每天都会生成大量的日志或数据。随着系统的发展，将调试数据存储到数据库中是不可行的，因为它们是不可变的，并且只能用于分析和解决故障。所以大部分公司倾向于将日志存储在文件中，而这些文件通常位于本地磁盘中。<br>
<br>我们将使用Go语言，从一个大小为16GB的<code class="prettyprint">.txt</code>或<code class="prettyprint">.log</code>文件中提取日志。<br>
<br>让我们开始编码……<br>
<br>首先，我们打开文件。对于任何文件的IO，我们都将使用标准的Go os.File。<br>
<pre class="prettyprint">f, err := os.Open(fileName)<br>
if err != nil &#123;<br>
fmt.Println("cannot able to read the file", err)<br>
return<br>
&#125;<br>
// UPDATE: close after checking error<br>
defer file.Close()  //Do not forget to close the file<br>
</pre><br>
打开文件后，我们有以下两个选项可以选择：<br>
<ol><li>逐行读取文件，这有助于减少内存紧张，但需要更多的时间。</li><li>一次将整个文件读入内存并处理该文件，这将消耗更多内存，但会显著减少时间。</li></ol><br>
<br>由于文件太大，即16 GB，因此无法将整个文件加载到内存中。但是第一种选择对我们来说也是不可行的，因为我们希望在几秒钟内处理文件。<br>
<br>但你猜怎么着，还有第三种选择。瞧……相比于将整个文件加载到内存中，在Go语言中，我们还可以使用<code class="prettyprint">bufio.NewReader()</code>将文件分块加载。<br>
<pre class="prettyprint">r := bufio.NewReader(f)<br>
for &#123;<br>
buf := make([]byte,4*1024) //the chunk size<br>
n, err := r.Read(buf) //loading chunk into buffer<br>
buf = buf[:n]<br>
if n == 0 &#123;<br>
<br>
 if err != nil &#123;<br>
   fmt.Println(err)<br>
   break<br>
 &#125;<br>
 if err == io.EOF &#123;<br>
   break<br>
 &#125;<br>
 return err<br>
&#125;<br>
&#125; <br>
</pre><br>
一旦我们将文件分块，我们就可以分叉一个线程，即<code class="prettyprint">Go routine</code>，同时处理多个文件区块。上述代码将修改为：<br>
<pre class="prettyprint">//sync pools to reuse the memory and decrease the preassure on Garbage Collector<br>
linesPool := sync.Pool&#123;New: func() interface&#123;&#125; &#123;<br>
    lines := make([]byte, 500*1024)<br>
    return lines<br>
&#125;&#125;<br>
stringPool := sync.Pool&#123;New: func() interface&#123;&#125; &#123;<br>
      lines := ""<br>
      return lines<br>
&#125;&#125;<br>
slicePool := sync.Pool&#123;New: func() interface&#123;&#125; &#123;<br>
       lines := make([]string, 100)<br>
       return lines<br>
&#125;&#125;<br>
r := bufio.NewReader(f)<br>
var wg sync.WaitGroup //wait group to keep track off all threads<br>
for &#123;<br>
<br>
 buf := linesPool.Get().([]byte)<br>
 n, err := r.Read(buf)<br>
 buf = buf[:n]<br>
if n == 0 &#123;<br>
    if err != nil &#123;<br>
        fmt.Println(err)<br>
        break<br>
    &#125;<br>
    if err == io.EOF &#123;<br>
        break<br>
    &#125;<br>
    return err<br>
 &#125;<br>
nextUntillNewline, err := r.ReadBytes('\n')//read entire line<br>
<br>
 if err != io.EOF &#123;<br>
     buf = append(buf, nextUntillNewline...)<br>
 &#125;<br>
<br>
 wg.Add(1)<br>
 go func() &#123; <br>
<br>
    //process each chunk concurrently<br>
    //start -> log start time, end -> log end time<br>
<br>
    ProcessChunk(buf, &linesPool, &stringPool, &slicePool,     start, end)<br>
wg.Done()<br>
<br>
 &#125;()<br>
&#125;<br>
wg.Wait()<br>
&#125; <br>
</pre><br>
上面的代码，引入了两个优化点：<br>
<ol><li><code class="prettyprint">sync.Pool</code>是一个强大的对象池，可以重用对象来减轻垃圾收集器的压力。我们将重用各个分片的内存，以减少内存消耗，大大加快我们的工作。</li><li><strong>Go Routines</strong>帮助我们同时处理缓冲区块，这大大提高了处理速度。</li></ol><br>
<br>现在让我们实现<strong>ProcessChunk</strong>函数，它将处理以下格式的日志行。<br>
<pre class="prettyprint">2020-01-31T20:12:38.1234Z, Some Field, Other Field, And so on, Till new line,...\n<br>
</pre><br>
我们将根据命令行提供的时间戳提取日志。<br>
<pre class="prettyprint">func ProcessChunk(chunk []byte, linesPool *sync.Pool, stringPool *sync.Pool, slicePool *sync.Pool, start time.Time, end time.Time) &#123;<br>
//another wait group to process every chunk further                             <br>
  var wg2 sync.WaitGroup<br>
logs := stringPool.Get().(string)<br>
logs = string(chunk)<br>
linesPool.Put(chunk) //put back the chunk in pool<br>
//split the string by "\n", so that we have slice of logs<br>
  logsSlice := strings.Split(logs, "\n")<br>
stringPool.Put(logs) //put back the string pool<br>
chunkSize := 100 //process the bunch of 100 logs in thread<br>
n := len(logsSlice)<br>
noOfThread := n / chunkSize<br>
if n%chunkSize != 0 &#123; //check for overflow <br>
     noOfThread++<br>
  &#125;<br>
length := len(logsSlice)<br>
//traverse the chunk<br>
 for i := 0; i < length; i += chunkSize &#123;<br>
<br>
     wg2.Add(1)<br>
//process each chunk in saperate chunk<br>
     go func(s int, e int) &#123;<br>
        for i:= s; i<e;i++&#123;<br>
           text := logsSlice[i]<br>
if len(text) == 0 &#123;<br>
              continue<br>
           &#125;<br>
<br>
        logParts := strings.SplitN(text, ",", 2)<br>
        logCreationTimeString := logParts[0]<br>
        logCreationTime, err := time.Parse("2006-01-  02T15:04:05.0000Z", logCreationTimeString)<br>
if err != nil &#123;<br>
             fmt.Printf("\n Could not able to parse the time :%s       for log : %v", logCreationTimeString, text)<br>
             return<br>
        &#125;<br>
// check if log's timestamp is inbetween our desired period<br>
      if logCreationTime.After(start) && logCreationTime.Before(end) &#123;<br>
<br>
        fmt.Println(text)<br>
       &#125;<br>
    &#125;<br>
    textSlice = nil<br>
    wg2.Done()<br>
<br>
 &#125;(i*chunkSize, int(math.Min(float64((i+1)*chunkSize), float64(len(logsSlice)))))<br>
//passing the indexes for processing<br>
&#125;  <br>
wg2.Wait() //wait for a chunk to finish<br>
logsSlice = nil<br>
&#125; <br>
</pre><br>
对上面的代码进行基准测试。以16 GB的日志文件为例，提取日志所需的时间约为25秒。<br>
<br>完整的代码示例如下：<br>
<pre class="prettyprint">func main() &#123;<br>
<br>
s := time.Now()<br>
args := os.Args[1:]<br>
if len(args) != 6 &#123; // for format  LogExtractor.exe -f "From Time" -t "To Time" -i "Log file directory location"<br>
    fmt.Println("Please give proper command line arguments")<br>
    return<br>
&#125;<br>
startTimeArg := args[1]<br>
finishTimeArg := args[3]<br>
fileName := args[5]<br>
<br>
file, err := os.Open(fileName)<br>
<br>
if err != nil &#123;<br>
    fmt.Println("cannot able to read the file", err)<br>
    return<br>
&#125;<br>
<br>
defer file.Close() //close after checking err<br>
<br>
queryStartTime, err := time.Parse("2006-01-02T15:04:05.0000Z", startTimeArg)<br>
if err != nil &#123;<br>
    fmt.Println("Could not able to parse the start time", startTimeArg)<br>
    return<br>
&#125;<br>
<br>
queryFinishTime, err := time.Parse("2006-01-02T15:04:05.0000Z", finishTimeArg)<br>
if err != nil &#123;<br>
    fmt.Println("Could not able to parse the finish time", finishTimeArg)<br>
    return<br>
&#125;<br>
<br>
filestat, err := file.Stat()<br>
if err != nil &#123;<br>
    fmt.Println("Could not able to get the file stat")<br>
    return<br>
&#125;<br>
<br>
fileSize := filestat.Size()<br>
offset := fileSize - 1<br>
lastLineSize := 0<br>
<br>
for &#123;<br>
    b := make([]byte, 1)<br>
    n, err := file.ReadAt(b, offset)<br>
    if err != nil &#123;<br>
        fmt.Println("Error reading file ", err)<br>
        break<br>
    &#125;<br>
    char := string(b[0])<br>
    if char == "\n" &#123;<br>
        break<br>
    &#125;<br>
    offset--<br>
    lastLineSize += n<br>
&#125;<br>
<br>
lastLine := make([]byte, lastLineSize)<br>
_, err = file.ReadAt(lastLine, offset+1)<br>
<br>
if err != nil &#123;<br>
    fmt.Println("Could not able to read last line with offset", offset, "and lastline size", lastLineSize)<br>
    return<br>
&#125;<br>
<br>
logSlice := strings.SplitN(string(lastLine), ",", 2)<br>
logCreationTimeString := logSlice[0]<br>
<br>
lastLogCreationTime, err := time.Parse("2006-01-02T15:04:05.0000Z", logCreationTimeString)<br>
if err != nil &#123;<br>
    fmt.Println("can not able to parse time : ", err)<br>
&#125;<br>
<br>
if lastLogCreationTime.After(queryStartTime) && lastLogCreationTime.Before(queryFinishTime) &#123;<br>
    Process(file, queryStartTime, queryFinishTime)<br>
&#125;<br>
<br>
fmt.Println("\nTime taken - ", time.Since(s))<br>
&#125;<br>
<br>
func Process(f *os.File, start time.Time, end time.Time) error &#123;<br>
<br>
linesPool := sync.Pool&#123;New: func() interface&#123;&#125; &#123;<br>
    lines := make([]byte, 250*1024)<br>
    return lines<br>
&#125;&#125;<br>
<br>
stringPool := sync.Pool&#123;New: func() interface&#123;&#125; &#123;<br>
    lines := ""<br>
    return lines<br>
&#125;&#125;<br>
<br>
r := bufio.NewReader(f)<br>
<br>
var wg sync.WaitGroup<br>
<br>
for &#123;<br>
    buf := linesPool.Get().([]byte)<br>
<br>
    n, err := r.Read(buf)<br>
    buf = buf[:n]<br>
<br>
    if n == 0 &#123;<br>
        if err != nil &#123;<br>
            fmt.Println(err)<br>
            break<br>
        &#125;<br>
        if err == io.EOF &#123;<br>
            break<br>
        &#125;<br>
        return err<br>
    &#125;<br>
<br>
    nextUntillNewline, err := r.ReadBytes('\n')<br>
<br>
    if err != io.EOF &#123;<br>
        buf = append(buf, nextUntillNewline...)<br>
    &#125;<br>
<br>
    wg.Add(1)<br>
    go func() &#123;<br>
        ProcessChunk(buf, &linesPool, &stringPool, start, end)<br>
        wg.Done()<br>
    &#125;()<br>
<br>
&#125;<br>
<br>
wg.Wait()<br>
return nil<br>
&#125;<br>
<br>
func ProcessChunk(chunk []byte, linesPool *sync.Pool, stringPool *sync.Pool, start time.Time, end time.Time) &#123;<br>
<br>
var wg2 sync.WaitGroup<br>
<br>
logs := stringPool.Get().(string)<br>
logs = string(chunk)<br>
<br>
linesPool.Put(chunk)<br>
<br>
logsSlice := strings.Split(logs, "\n")<br>
<br>
stringPool.Put(logs)<br>
<br>
chunkSize := 300<br>
n := len(logsSlice)<br>
noOfThread := n / chunkSize<br>
<br>
if n%chunkSize != 0 &#123;<br>
    noOfThread++<br>
&#125;<br>
<br>
for i := 0; i < (noOfThread); i++ &#123;<br>
<br>
    wg2.Add(1)<br>
    go func(s int, e int) &#123;<br>
        defer wg2.Done() //to avaoid deadlocks<br>
        for i := s; i < e; i++ &#123;<br>
            text := logsSlice[i]<br>
            if len(text) == 0 &#123;<br>
                continue<br>
            &#125;<br>
            logSlice := strings.SplitN(text, ",", 2)<br>
            logCreationTimeString := logSlice[0]<br>
<br>
            logCreationTime, err := time.Parse("2006-01-02T15:04:05.0000Z", logCreationTimeString)<br>
            if err != nil &#123;<br>
                fmt.Printf("\n Could not able to parse the time :%s for log : %v", logCreationTimeString, text)<br>
                return<br>
            &#125;<br>
<br>
            if logCreationTime.After(start) && logCreationTime.Before(end) &#123;<br>
                //fmt.Println(text)<br>
            &#125;<br>
        &#125;<br>
<br>
<br>
    &#125;(i*chunkSize, int(math.Min(float64((i+1)*chunkSize), float64(len(logsSlice)))))<br>
&#125;<br>
<br>
wg2.Wait()<br>
logsSlice = nil<br>
&#125; <br>
</pre><br>
<br><strong>原文链接：<a href="https://medium.com/swlh/processing-16gb-file-in-seconds-go-lang-3982c235dfa2">Reading 16GB File in Seconds, Golang</a>  （翻译：钟涛）</strong>
                                
                                                              
</div>
            