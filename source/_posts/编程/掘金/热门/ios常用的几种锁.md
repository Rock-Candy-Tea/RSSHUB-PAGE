
---
title: 'ios常用的几种锁'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a83f5c9d9514a86ae264bdd2b1a63ae~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 00:43:23 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a83f5c9d9514a86ae264bdd2b1a63ae~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>开发中引入了异步和多线程的来提高程序性能，也就意味着线程安全成为了多线程的一个障碍，因此线程锁应运而生，而锁如果用不好，还会造成死锁的风险</p>
<p>下面就介绍ios中常用的几种锁，以及读写锁的实现</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMarshal-S%2FLockDemo.git" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Marshal-S/LockDemo.git" ref="nofollow noopener noreferrer">案例demo</a></p>
<h2 data-id="heading-1">常见的多线程锁</h2>
<p>ios中常见的几种锁包括OSSpinLock、信号量(Semaphore)、pthread_mutex、NSLock、NSCondition、NSConditionLock、pthread_mutex(recursive)、NSRecursiveLock、synchronized</p>
<p>如下所示，为前辈们测试锁性能的案例图(实际可能会略有偏差)：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a83f5c9d9514a86ae264bdd2b1a63ae~tplv-k3u1fbpfcp-watermark.image" alt="1899027-eb3ef0d444034362.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于OSSpinLock目前已经不再安全，这里就放弃介绍，案例也把他给删了😂</p>
<p>我们再选锁的时候，如果只是使用互斥锁的效果，那么按照性能排序选择靠前的即可，如果需要锁的一些其他功能，那么根据需要选择，不必过于局限于性能，毕竟实现功能与项目的维护也是非常重要的</p>
<p>其他锁的使用如下所示</p>
<h3 data-id="heading-2">信号量(semaphore)</h3>
<p>信号量实现加锁功能与其他的略有不同，其通过一个信号值来决定是否阻塞当前线程</p>
<p>wait操作可以使得信号量值减少1，signal使得信号量值增加1</p>
<p>当wait操作使得信号量值小于0时，则所在线程阻塞阻塞休眠，使用signal使得信号量增加时，会顺序唤醒阻塞线程，以此便可以实现加锁功能,</p>
<pre><code class="hljs language-js copyable" lang="js">- (<span class="hljs-keyword">void</span>)semaphore &#123;
    _semaphore = dispatch_semaphore_create(<span class="hljs-number">1</span>);
&#125;

<span class="hljs-comment">//wait操作可以使得信号量值减少1，signal使得信号量值增加1</span>
<span class="hljs-comment">//当信号量值小于0时，则所在线程阻塞休眠，使用signal使得信号量增加时，会顺序唤醒阻塞线程</span>
- (<span class="hljs-keyword">void</span>)semaphoreUpdate &#123;
    <span class="hljs-comment">//wait 可以理解为加锁操作，信号值小于0会休眠当前wait所在线程</span>
    <span class="hljs-comment">//第二个参数 forever 为永远，可以自行设置一段超时时间，达到等待时间会自动解锁</span>
    dispatch_semaphore_wait(_semaphore, DISPATCH_TIME_FOREVER);
    
    wait和singnal中间的这部分代码,即为线程安全代码
    _money++;
    
    <span class="hljs-comment">//signal 可以解锁</span>
    dispatch_semaphore_signal(_semaphore);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">pthread互斥锁</h3>
<p>pthread互斥锁是 <code>pthread</code> 库中的一员，<code>linux</code>系统中中常用的库,使用时需要手动import导入 <code>#import <pthread/pthread.h></code></p>
<p>其中有 <code>pthread_mutex_trylock</code>为尝试加锁，如果没被加锁，则会加锁成功，并返回0，适用于一些优先级比较低，间歇性调用的功能</p>
<p><strong>注意</strong>：其他部分锁也有<code>trylock</code>这个功能，例如 <code>NSLock、NSRecursiveLock、NSConditionLock</code></p>
<pre><code class="hljs language-js copyable" lang="js">#pragma mark --pthread互斥锁
- (<span class="hljs-keyword">void</span>)pthreadMutex &#123;
    pthread_mutex_init(&_pMutexLock, NULL);
    <span class="hljs-comment">//使用完毕后在合适的地方销毁，例如dealloc</span>
<span class="hljs-comment">//    pthread_mutex_destroy(&_pMutexLock);</span>
&#125;

- (<span class="hljs-keyword">void</span>)pthreadMutexUpdate &#123;
    <span class="hljs-comment">//加锁代码区间操作，避免多线程同时访问</span>
    pthread_mutex_lock(&_pMutexLock);
    _money++;
    <span class="hljs-comment">//解锁代码区间操作</span>
    pthread_mutex_unlock(&_pMutexLock);
&#125;

- (<span class="hljs-keyword">void</span>)pthreadMutexSub &#123;
    <span class="hljs-comment">//减少数值</span>
    [NSThread detachNewThreadWithBlock:^&#123;
        <span class="hljs-comment">//数量大于100开始减少，假设是需要清理东西，这里减少数值</span>
        <span class="hljs-keyword">while</span> (self->_money > <span class="hljs-number">10000</span>) &#123;
            <span class="hljs-comment">//尝试加锁，如果能加锁，则加锁，返回零，否则返回不为零的数字</span>
            <span class="hljs-comment">//加锁失败休眠在执行，避免抢夺资源，此任务优先级间接降低</span>
            <span class="hljs-comment">//其他的一些锁也有这功能,例如NSLock、NSRecursiveLock、NSConditionLock</span>
            <span class="hljs-keyword">if</span> (pthread_mutex_trylock(&self->_pMutexLock) == <span class="hljs-number">0</span>) &#123;
                self->_money--;
                <span class="hljs-comment">//解锁</span>
                pthread_mutex_unlock(&self->_pMutexLock);
            &#125;<span class="hljs-keyword">else</span> &#123;
                [NSThread sleepForTimeInterval:<span class="hljs-number">1</span>];
            &#125;
        &#125;
    &#125;];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">NSLock互斥锁</h3>
<p>NSLock 遵循 <code>NSLocking协议</code>,是常见的互斥锁之一，为 OC 框架中的 API，使用方便，据说是 pthread 封装的锁</p>
<p><code>tryLock</code> 方法也是尝试加锁，成功返回true，失败返回false</p>
<p><code>lockBeforeDate:(NSDate *)limit</code> 在一个时间之间加锁，可以理解为加锁日期截止到指定时间，会自动解锁(与信号量的等待功能一样，这个是设置到指定时间)</p>
<pre><code class="hljs language-js copyable" lang="js">#pragma mark --NSLock互斥锁
- (<span class="hljs-keyword">void</span>)NSLock &#123;
    _lock = [[NSLock alloc] init];
&#125;

- (<span class="hljs-keyword">void</span>)NSLockUpdate &#123;
    <span class="hljs-comment">//加锁代码区间，避免多线程同时访问</span>
    [_lock lock];
    _money++;
    <span class="hljs-comment">//解锁代码区间</span>
    [_lock unlock];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">NSCondition锁</h3>
<p>NSCondition 算是一个稍微重量级的锁了，我理解为<code>情景锁</code>(另一个原因区分条件锁 <code>NSConditionLock</code>)，适用于一些特殊场景，其也遵循 <code>NSLocking</code>协议，也属于互斥锁</p>
<p>并且再其基础上，新增了信号量功能 <code>wait</code>和 <code>signal</code>，即 等待 和 释放 ，使用方式和 <code>semaphore</code> 一样，可以通过信号量控制线程的阻塞和释放，除此之外，还多了一个<code>broadcast</code>，其可以解除所有因 wait 阻塞的线程</p>
<p>如下所示，使用 <code>NSCondition</code> 实现了一个生产者和消费者的案例（生产者和消费者都是同一拨人，因此需要加锁来实现，而为了保证有钱了立刻买自己想买的东西，使用信号量，保证没钱时阻塞等待，有钱时立即解放买买买）</p>
<p>其相当于同时使用了<code>NSLock 和 Semaphore</code> 功能</p>
<pre><code class="hljs language-js copyable" lang="js">#pragma mark --情景锁NSCondition实现了NSLocking协议，支持默认的互斥锁lock、unlock
- (<span class="hljs-keyword">void</span>)NSCondition &#123;
    _condition = [[NSCondition alloc] init];
&#125;

<span class="hljs-comment">//情景锁还加入了信号量机制,wait和signal，可以利用其完成生产消费者模式的功能</span>
<span class="hljs-comment">//生产者: 妈爸挣了一天的钱，储蓄值增加</span>
- (<span class="hljs-keyword">void</span>)conditionPlusMoney &#123;
    [_condition lock];
    <span class="hljs-comment">//信号量增加，有储蓄了，可以开放花钱功能了</span>
    <span class="hljs-keyword">if</span> (_money++ < <span class="hljs-number">0</span>) &#123;
        [_condition signal];    <span class="hljs-comment">//释放第一个阻塞的线程</span>
        <span class="hljs-comment">//[_condition broadcast]; //释放所有阻塞的线程</span>
    &#125;
    [_condition unlock];
&#125;
<span class="hljs-comment">//消费者，服务有储蓄，拿到钱时立即解锁花钱技能(money--)</span>
- (<span class="hljs-keyword">void</span>)conditionSubMoney &#123;
    [_condition lock];
    <span class="hljs-keyword">if</span> (_money == <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">//信号量减少阻塞，打算买东西，却没钱了，停止花钱，等发工资再买东西</span>
        [_condition wait];
    &#125;
    <span class="hljs-comment">//由于之前的wait，当signal解锁后，会走到这里，开始购买想买的东西，储蓄值--</span>
    _money--;
    [_condition unlock];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">NSConditionLock</h3>
<p>NSConditionLock 被称为条件锁，其遵循 <code>NSLocking</code> 协议，即具备正常的互斥锁功能</p>
<p>此外加入了 条件语句，为其核心功能，即满足指定条件才会解锁，因此算是一个重量级的锁了，其同时可以理解为 <code>NSCondition 进化版</code> ，如果你理解了 <code>NSCondition</code>的<code>生产者-消费者</code>模式，这个也会马上就明白了其原理了</p>
<p><code>lockWhenCondition:(NSInteger)condition</code>: 加锁，当条件condition为传入的condition时，方能解锁</p>
<p><code>unlockWithCondition:(NSInteger)condition</code>: 更新condition的值，并解锁指定condition的锁</p>
<p>下面使用一个异步队列，来实现类似 NSOperation 设置的依赖关系，如下所示(打印结果1、4、3、2)：</p>
<pre><code class="hljs language-js copyable" lang="js">#pragma mark --条件锁NSConditionLock,实现了NSLocking协议，支持默认的互斥锁lock、unlock
- (<span class="hljs-keyword">void</span>)NSConditionLock &#123;
    _conditionLock = [[NSConditionLock alloc] initWithCondition:<span class="hljs-number">1</span>]; <span class="hljs-comment">//可以更改值测试为0测试结果</span>
    <span class="hljs-comment">//加锁，当条件condition为传入的condition时，方能解锁</span>
    <span class="hljs-comment">//lockWhenCondition:(NSInteger)condition</span>
    <span class="hljs-comment">//更新condition的值，并解锁指定condition的锁</span>
    <span class="hljs-comment">//unlockWithCondition:(NSInteger)condition</span>
&#125;

<span class="hljs-comment">//多个队列执行条件锁</span>
<span class="hljs-comment">//通过案例可以看出，通过条件锁conditionLock可以设置线程依赖关系</span>
<span class="hljs-comment">//可以通过GCD设置一个具有依赖关系的任务队列么</span>
- (<span class="hljs-keyword">void</span>)NSConditionLockUpdate &#123;
    <span class="hljs-comment">//创建并发队列</span>
    dispatch_queue_t queue = 
        dispatch_queue_create(<span class="hljs-string">"测试NSConditionLock"</span>, DISPATCH_QUEUE_CONCURRENT);
    dispatch_async(queue, ^&#123;
        <span class="hljs-keyword">if</span> ([self->_conditionLock tryLockWhenCondition:<span class="hljs-number">1</span>]) &#123;
            NSLog(@<span class="hljs-string">"第一个"</span>);
            <span class="hljs-comment">//默认初始conditon位1，所有能走到这里</span>
            <span class="hljs-comment">//然后解锁后，并设置初始值为4，解锁condition设定为4的线程</span>
            [self->_conditionLock unlockWithCondition:<span class="hljs-number">4</span>];
        &#125;<span class="hljs-keyword">else</span> &#123;
            [self->_conditionLock lockWhenCondition:<span class="hljs-number">0</span>];
            NSLog(@<span class="hljs-string">"第一个other"</span>);
            [self->_conditionLock unlockWithCondition:<span class="hljs-number">4</span>];
        &#125;
    &#125;);
    <span class="hljs-comment">//由于开始初始化的conditon值为1，所以后面三个线程都不满足条件</span>
    <span class="hljs-comment">//锁定后直到condition调整为当前线程的condition时方解锁</span>
    dispatch_async(queue, ^&#123;
        <span class="hljs-comment">//condition设置为3后解锁当前线程</span>
        [self->_conditionLock lockWhenCondition:<span class="hljs-number">2</span>];
        NSLog(@<span class="hljs-string">"第二个"</span>);
        <span class="hljs-comment">//执行完毕后解锁，并设置condition为1，设置初始化默认值，以便于下次使用</span>
        [self->_conditionLock unlockWithCondition:<span class="hljs-number">1</span>];
    &#125;);
    dispatch_async(queue, ^&#123;
        <span class="hljs-comment">//condition设置为3后解锁当前线程</span>
        [self->_conditionLock lockWhenCondition:<span class="hljs-number">3</span>];
        NSLog(@<span class="hljs-string">"第三个"</span>);
        <span class="hljs-comment">//执行完毕后解锁，并设置condition为3，解锁3</span>
        [self->_conditionLock unlockWithCondition:<span class="hljs-number">2</span>];
    &#125;);
    dispatch_async(queue, ^&#123;
        <span class="hljs-comment">//condition设置为4后解锁当前线程</span>
        [self->_conditionLock lockWhenCondition:<span class="hljs-number">4</span>];
        NSLog(@<span class="hljs-string">"第四个"</span>);
        <span class="hljs-comment">//执行完毕后解锁，并设置condition为3，解锁3</span>
        [self->_conditionLock unlockWithCondition:<span class="hljs-number">3</span>];
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的流程可以大致简化为下面几步：</p>
<p>1.创建一个异步队列，以便于添加后续的任务依赖</p>
<p>2.逐步添加子任务模块，分别在不同线程中，其有明确的依赖关系，即执行顺序为 1、4、3、2</p>
<p>3.使用 <code>lockWhenCondition：</code>开始设置依赖，将其任务<code>解锁的条件condition</code> 设置为其<code>特有的condition 号</code>，以便于解锁</p>
<p>4.执行任务时，如果 <code>NSCondition 中的 condition 参数</code>，与<code>本线程设置的tCondition</code>不一样时，阻塞线程，等待 <code>NSCondition 中的 condition</code> 更改为指定值(通过 <code>unlockWithCondition:</code>更改condition值)解锁</p>
<p>即：默认初始化 condition 为 1，只有 <code>任务1</code> 能够执行，当 <code>任务1</code> 执行 <code>unlockWithCondition:4</code>时，condition被设置为4, <code>阻塞的任务4</code>解锁，同理，<code>任务4</code>执行完毕后，将 condition 设置为 3 ,任务三解锁，依次类推</p>
<p>5.最终根据设置的依赖关系，分别执行 任务1、任务4、任务3、任务2</p>
<h3 data-id="heading-7">pthread_mutex(recursive)</h3>
<p>其为基于 <code>pthread框架</code> 的递归锁，也是以 <code>pthread互斥锁为基础</code>实现的 <code>递归锁</code>，即：同一个线程下，递归调用时加锁，不会阻塞当前线程，当另一个线程到来时，会因为第一个线程加的锁而阻塞</p>
<pre><code class="hljs language-js copyable" lang="js">#pragma mark --pthread递归锁
- (<span class="hljs-keyword">void</span>)pthreadMutexRecursive &#123;
    <span class="hljs-comment">//初始化锁的递归功能</span>
    pthread_mutexattr_t attr;
    pthread_mutexattr_init(&attr);
    pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_RECURSIVE);
    <span class="hljs-comment">//互斥锁初始化时，绑定递归锁功能模块</span>
    pthread_mutex_init(&_pMutexLock, &attr);
    
    <span class="hljs-comment">//使用完毕后在合适的地方销毁，例如dealloc</span>
<span class="hljs-comment">//    pthread_mutexattr_destroy(&attr);</span>
<span class="hljs-comment">//    pthread_mutex_destroy(&_pMutexLock);</span>
&#125;

<span class="hljs-comment">//使用递归锁，递归地时候回不停加锁，如果使用普通的锁早已经形成死锁，无法解脱</span>
<span class="hljs-comment">//递归锁的存在就是在同一个线程中的锁，不会互斥，只会互斥其他线程的锁，从而避免死锁</span>
- (<span class="hljs-keyword">void</span>)pthreadMutexRecursiveUpdate &#123;
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, <span class="hljs-number">0</span>), ^&#123;
        <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> (^recursiveBlock)(double count);
        recursiveBlock = ^(double count)&#123;
            pthread_mutex_lock(&self->_pMutexLock);
            <span class="hljs-keyword">if</span> (count-- > <span class="hljs-number">0</span>) &#123;
                self->_money++;
                recursiveBlock(count);
            &#125;
            pthread_mutex_unlock(&self->_pMutexLock);
        &#125;;
        recursiveBlock(<span class="hljs-number">1000</span>);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">NSRecursiveLock递归锁</h3>
<p>和 <code>pthread_mutex(recursive)</code>一样，NSRecursiveLock 也是递归锁，其遵循 <code>NSLocking</code> 协议，即除了递归锁功能，还具备正常的互斥锁功能</p>
<p>使用方式和 <code>pthread_mutex(recursive)</code>一样如下所示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//使用递归锁，递归地时候回不停加锁，如果使用普通的锁早已经形成死锁，无法解脱</span>
<span class="hljs-comment">//递归锁的存在就是在同一个线程中的锁，不会互斥，只会互斥其他线程的锁，从而避免死锁</span>
- (<span class="hljs-keyword">void</span>)NSRecursiveLockUpdate &#123;
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, <span class="hljs-number">0</span>), ^&#123;
        <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> (^recursiveBlock)(double count);
        recursiveBlock = ^(double count)&#123;
            [self->_recursive lock];
            <span class="hljs-comment">//tryLock就不多介绍了，和Pthread的类似，注意返回值即可</span>
            <span class="hljs-comment">//[self->_recursive tryLock];</span>
            <span class="hljs-keyword">if</span> (count-- > <span class="hljs-number">0</span>) &#123;
                self->_money++;
                recursiveBlock(count);
            &#125;
            [self->_recursive unlock];
        &#125;;
        recursiveBlock(<span class="hljs-number">1000</span>);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">synchronized</h3>
<p>synchronized 同步锁，即同步执行，以此避免多线程同时操作同一块代码，基本上在各个平台都会有其身影，虽然效率最低，但由于使用使用简单，深得大家喜爱</p>
<p>实现如下所示</p>
<pre><code class="hljs language-js copyable" lang="js">#pragma mark --同步锁synchronized
- (<span class="hljs-keyword">void</span>)synchronized &#123;
    <span class="hljs-comment">//使用简单，直接对代码块加同步锁，此代码不会被多个线程直接执行</span>
    <span class="hljs-comment">//可以间接理解为里面的任务被放到了一个同步队列依次执行（实际实现未知）</span>
    @synchronized (self) &#123;
        self->_money++;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">读写锁</h2>
<p><code>读写锁</code> 又被称为 <code>rw锁</code>或者 <code>readwrite锁</code>，在 ios开发中虽能见到，但确不是最常用的(一般是数据库操作才会用到)。</p>
<p>具体操作为：<code>多读单写</code>，即，写入操作只能串行执行，且写入时，不能读取，而读取需支持多线程操作，且读取时，不能写入</p>
<p>相信大家也遇到过这样的事，系统的属性设置了 <code>auto</code>参数，字面意思为原子性操作，其实际未能保证属性字段的多线程安全(由于旧值的赋值未加锁，同时写入时，会造成对象旧地址多次被release)</p>
<p>因此无论是想了解其实现方式，还是开发备用，都是有比较学习的</p>
<p>实现方式这里就提供两种：pthread、GCD的barrier来实现</p>
<h3 data-id="heading-11">pthread读写锁</h3>
<p>使用前，需要先导入 <code>pthread框架</code>, 即 <code>#import <pthread/pthread.h></code></p>
<p>实现简单，可以根据自己程序需要，选择锁初始化的合适位置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//初始化pthread读写锁</span>
- (<span class="hljs-keyword">void</span>)setupPhreadRW &#123;
    pthread_rwlock_init(&_lock, NULL);
    <span class="hljs-comment">//使用完毕销毁读写锁</span>
    <span class="hljs-comment">//pthread_rwlock_destroy(&_lock);</span>
&#125;

#pragma mark --通过pthread读写锁来设置
- (<span class="hljs-keyword">void</span>)setLock1:(NSString *)lock1 &#123;
    pthread_rwlock_wrlock(&_lock);
    _lock1 = lock1;
    pthread_rwlock_unlock(&_lock);
    
&#125;
- (NSString *)lock1 &#123;
    NSString *lock1 = nil;
    pthread_rwlock_rdlock(&_lock);
    lock1 = [_lock1 copy]; <span class="hljs-comment">//copy到新的地址,避免解锁后拿到旧值</span>
    pthread_rwlock_unlock(&_lock);
    <span class="hljs-keyword">return</span> lock1;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">GCD的barrier读写锁</h3>
<p>GCD的barrier栅栏功能相信大家都听说过，即在一个新创建的队列中，barrier功能可以保证，在他之前的异步队列执行完毕才指定barrier中间的内容，且还能保证barrier执行完毕后，才之后barrier之后的任务，且一个队列可以有多个barrier</p>
<p>因此此特性可以用于完成一个读写锁功能，即 barrier的代码块作为 写入操作模块</p>
<p>如下代码所示，由于需要引入 新创建队列，虽然使用起来不是不如pthread优秀，但这种思想却可以再恰当的时候发芽出新树苗</p>
<pre><code class="hljs language-js copyable" lang="js">- (<span class="hljs-keyword">void</span>)setupGCDRW &#123;
    _queue = dispatch_queue_create(<span class="hljs-string">"RWLockQueue"</span>, DISPATCH_QUEUE_CONCURRENT);
&#125;

#pragma mark --通过GCD的barrier栅栏功能实现
<span class="hljs-comment">//通过GCD的barrier栅栏功能实现，缺点是需要借助自定义队列实现，且get方法无法重写系统的，只能以回调的方式获取值</span>
<span class="hljs-comment">//barrier功能使用global队列会失效，全局队列是无法阻塞的，里面有系统的一些任务执行</span>
- (<span class="hljs-keyword">void</span>)setLock2:(NSString *)lock2 &#123;
    dispatch_barrier_async(_queue, ^&#123;
        self->_lock2 = lock2;
    &#125;);
&#125;
- (<span class="hljs-keyword">void</span>)getLock2WithBlock:(<span class="hljs-keyword">void</span>(^)(NSString *))block &#123;
    dispatch_async(_queue, ^&#123;
        block(self->_lock2);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">最后</h2>
<p>相信看了这篇文章能给大家带来更多收货</p>
<p>最后，你能根据读写锁的特性，利用现有的锁，再写出一个完整的读写锁功能出来么!</p></div>  
</div>
            