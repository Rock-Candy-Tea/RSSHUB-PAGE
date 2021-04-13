
---
title: 'etcd分布式锁内存泄露'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/eda32e45146be5cf0748d713b38e75aa.jpeg'
author: Dockone
comments: false
date: 2021-04-13 00:28:28
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/eda32e45146be5cf0748d713b38e75aa.jpeg'
---

<div>   
<br><h3>背景</h3>通过监控看到云平台后端程序的内存使用量在稳定增加，每次上线完又会恢复，基本可以断定程序存在内存泄漏问题（可以用memleak检测，memleak是基于ebpf的一个bcc工具）。<br>
<h3>排查过程</h3>Golang程序的问题排查，无论CPU还是Memory问题都可以用官方提供的pprof工具，最简单的办法就是在代码加入如下包net/http/pprof，上线到了测试环境，然后通过go tool pprof httpaddress的方式查看内存消耗，网上也有很多pprof使用方法的文章，可以自行搜索，知道怎么用了之后看下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/eda32e45146be5cf0748d713b38e75aa.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/eda32e45146be5cf0748d713b38e75aa.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
由于是测试环境，对接测试集群，本身数据量就不大，程序刚启动时占用内存也就百十来M，现在已经用了1G多，占用内存最多的是newWatcherGrpcStream函数，还有一些其他的函数，占用的内存也在逐步增加，先看newWatcherGrpcStream函数，可以通过list查看其具体内存使用情况，如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210409/10d6e3e1bb02545f81a2a24815d57c37.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210409/10d6e3e1bb02545f81a2a24815d57c37.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
fmt.Sprintf居然都占用了86.01M内存，还有几个chan占用的也比较多，但是基本都是无缓存的chan，正常不会占用这么多的。一般内存泄露可能是流未关闭，这种情况一般文件描述符也会泄露，另外就是用到缓存时也容易造成泄露，如果缓存的内容得不到释放且一直增加内容，内存就会越来越高。去看etcd相关代码，在代码中找问题，发现了一处很可疑的代码，去掉了无关内容，且增加了fmt.Println相关函数，方便观察每次运行到此处的缓存的结果，如下：<br>
<pre class="prettyprint">// Watch posts a watch request to run() and waits for a new watcher channel<br>
func (w *watcher) Watch(ctx context.Context, key string, opts ...OpOption) WatchChan &#123;<br>
...<br>
ctxKey := fmt.Sprintf("%v", ctx)<br>
<br>
// find or allocate appropriate grpc watch stream<br>
w.mu.Lock()<br>
if w.streams == nil &#123;<br>
  // closed<br>
  w.mu.Unlock()<br>
  ch := make(chan WatchResponse)<br>
  close(ch)<br>
  return ch<br>
&#125;<br>
fmt.Println(ctxKey)      // 打印缓存的key<br>
fmt.Println(len(w.streams))       //打印缓存数量<br>
wgs := w.streams[ctxKey]<br>
if wgs == nil &#123;<br>
  fmt.Println("new watcher stream")        //缓存里没有对应的key<br>
  wgs = w.newWatcherGrpcStream(ctx)<br>
  w.streams[ctxKey] = wgs<br>
&#125;else&#123;<br>
  fmt.Println("use exist watcher stream")  //缓存里有key，复用缓存<br>
&#125;<br>
...<br>
&#125;<br>
<br>
// watcher implements the Watcher interface<br>
type watcher struct &#123;<br>
remote pb.WatchClient<br>
<br>
// mu protects the grpc streams map<br>
mu sync.RWMutex<br>
<br>
// streams holds all the active grpc streams keyed by ctx value.<br>
streams map[string]*watchGrpcStream<br>
&#125; <br>
</pre><br>
这里出现了上面的fmt.Sprintf、newWatcherGrpcStream等函数，而且出现了缓存，即w.streams，每次watch时都是先调用fmt.Sprintf获取到key，再从缓存中取，如果有则复用，没有则新建，问题很有可能出现在这里，然后再找一下缓存删除数据的逻辑，如下：<br>
<pre class="prettyprint">func (w *watcher) Close() (err error) &#123;<br>
w.mu.Lock()<br>
fmt.Println("begin close watcher")<br>
streams := w.streams<br>
w.streams = nil<br>
w.mu.Unlock()<br>
for _, wgs := range streams &#123;<br>
  if werr := wgs.Close(); werr != nil &#123;<br>
     err = werr<br>
  &#125;<br>
&#125;<br>
return err<br>
&#125;<br>
<br>
func (w *watcher) closeStream(wgs *watchGrpcStream) &#123;<br>
w.mu.Lock()<br>
fmt.Println("delete watch stream") //开始删除缓存<br>
close(wgs.donec)<br>
wgs.cancel()<br>
if w.streams != nil &#123;<br>
  fmt.Println("before delete:",len(w.streams))      //删除前缓存数量<br>
  fmt.Println(wgs.ctxKey)<br>
  if _,ok:=w.streams[wgs.ctxKey];ok&#123;<br>
     fmt.Println("delete key exist")        //删除的key在缓存里存在<br>
  &#125;     else&#123;<br>
     fmt.Println("delete key NOT exist")    //删除的key在缓存里不存在<br>
  &#125;<br>
  delete(w.streams, wgs.ctxKey)<br>
  fmt.Println("after delete:",len(w.streams))       //删除后缓存的数量<br>
&#125;<br>
w.mu.Unlock()<br>
&#125; <br>
</pre><br>
和删除缓存相关的函数有两个，第一个Close函数只有在etcdclient的关闭链接时才会调用，而我们在不断的lock，unlock时其实用的是同一份etcdclient，所以不会是第一个函数。还剩一个closeStream函数，这里我也加了一些打印信息，用来查看缓存相关信息，closeStream调用如下：<br>
<pre class="prettyprint">func (w *watcher) newWatcherGrpcStream(inctx context.Context) *watchGrpcStream &#123;<br>
...<br>
go wgs.run()<br>
return wgs<br>
&#125;<br>
<br>
// run is the root of the goroutines for managing a watcher client<br>
func (w *watchGrpcStream) run() &#123;<br>
...<br>
<br>
defer func() &#123;<br>
  ...<br>
<br>
  w.owner.closeStream(w)<br>
&#125;()<br>
<br>
...<br>
&#125; <br>
</pre><br>
整个过程从插入缓存到删除缓存看起来都没有问题，只能写个demo测试一下了，demo大致如下：<br>
<pre class="prettyprint">func main() &#123;<br>
client := instance.GetEtcdClient()<br>
locker := lock.New(client, lock.WithTTL(1*time.Second))<br>
go foo(locker)<br>
http.HandleFunc("/gc", func(writer http.ResponseWriter, request *http.Request) &#123;<br>
  runtime.GC()<br>
&#125;)<br>
http.ListenAndServe(":8080", nil)<br>
&#125;<br>
<br>
func foo(locker lock.Locker) &#123;<br>
ticker := time.NewTicker(1 * time.Second)<br>
ids := []string&#123;"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"&#125;<br>
<br>
for range ticker.C &#123;<br>
  for _, v := range ids &#123;<br>
     go func(i string) &#123;<br>
        unlock, _, err := locker.Trylock(context.TODO(), fmt.Sprintf("%s/%s", "/kaku/test/etcd/lock", i))<br>
        if err != nil &#123;<br>
           if err != context.DeadlineExceeded &#123;<br>
              fmt.Println("lock task failed:%s", err)<br>
           &#125;<br>
           return<br>
        &#125;<br>
        //fmt.Println("task has been locked")<br>
        defer func() &#123;<br>
           time.Sleep(time.Second)<br>
           unlock()<br>
           //fmt.Println("task has been unlocked")<br>
        &#125;()<br>
     &#125;(v)<br>
  &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
特别简单，就是不断的去lock，unlock，结合之前增加的一些缓存打印信息，运行demo，结果如下：<br>
<pre class="prettyprint">context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293267 +0800 CST m=+3.078016721 [750.274218ms]).WithCancel<br>
0<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293375 +0800 CST m=+3.078124824 [704.968531ms]).WithCancel<br>
1<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293271 +0800 CST m=+3.078020710 [704.72989ms]).WithCancel<br>
2<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293342 +0800 CST m=+3.078090947 [704.058853ms]).WithCancel<br>
3<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293275 +0800 CST m=+3.078023966 [703.750266ms]).WithCancel<br>
4<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293282 +0800 CST m=+3.078031664 [703.519141ms]).WithCancel<br>
5<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293339 +0800 CST m=+3.078088098 [702.930648ms]).WithCancel<br>
6<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293454 +0800 CST m=+3.078203813 [688.620812ms]).WithCancel<br>
7<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293371 +0800 CST m=+3.078120807 [688.102422ms]).WithCancel<br>
8<br>
new watcher stream<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293341 +0800 CST m=+3.078090285 [688.007852ms]).WithCancel<br>
9<br>
new watcher stream<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293282 +0800 CST m=+3.078031664 [703.500369ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293371 +0800 CST m=+3.078120807 [688.080708ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293275 +0800 CST m=+3.078023966 [703.729632ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293342 +0800 CST m=+3.078090947 [704.033358ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293375 +0800 CST m=+3.078124824 [704.880537ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293341 +0800 CST m=+3.078090285 [687.986963ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293339 +0800 CST m=+3.078088098 [702.908025ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293267 +0800 CST m=+3.078016721 [750.193256ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
delete watch stream<br>
before delete: 10<br>
context.TODO.WithCancel.WithDeadline(2019-01-27 12:03:04.293271 +0800 CST m=+3.078020710 [704.644318ms]).WithCancel<br>
delete key NOT exist<br>
after delete: 10<br>
</pre><br>
看到每次复用缓存都会失败，而且删除缓存的key时，key都不存在，导致缓存的数量一直在增加，从而导致使用的内存越来越大。那为什么每次复用缓存和删除时都找不到对应的key呢，其实问题就出现在的缓存key的计算方法上。<br>
<pre class="prettyprint">ctxKey := fmt.Sprintf("%v", ctx)<br>
</pre><br>
简单，粗暴，直接格式化ctx作为缓存的key，那问题就来了，我们传入的ctx其实是context.WithTimeout后得到的，这个ctx格式化后会带事件输出，如上面的输出结果，同一个ctx，每次格式化输出得到的string其实是不一样的，而且这个key是每次用到的时候都去获取一次，并没有在第一次获取完就保存下来，所以就会导致每次获取缓存都没有这个key，删除时也没有，这就是问题所在了，也可以解释为什么fmt.Sprintf居然还会占用那么多内存的现象了。<br>
<br>目前用的3.1.3的etcd代码，直到3.2.20版本时获取key的方式才改变，但是当初要改变的获取key的方式的原因并非是发现了上述问题，而是之前的设计还存在另一个问题，即竞态问题，见<a href="https://link.zhihu.com/?target=https%3A//github.com/etcd-io/etcd/issues/8275"></a><a href="https://github.com/etcd-io/etcd/issues/8275" rel="nofollow" target="_blank">https://github.com/etcd-io/etcd/issues/8275</a>。无心插柳柳成荫，3.2.20版本解决了竞态问题后，上面分析的问题也就解决了。<br>
<h3>解决方案</h3>升级etcd包版本至少到3.2.20。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/z55QHeQYsHFjTx7Hq--Kdw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/z55QHeQYsHFjTx7Hq--Kdw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            