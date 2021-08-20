
---
title: 'Android Jetpack系列--7. WorkManager使用详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=465'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 02:39:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=465'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">相关知识</h3>
<ul>
<li>交换空间：当系统内存资源已被耗尽，但是又有额外的内存资源请求的时候，内存中不活动的页面会被移动到交换空间。交换空间是磁盘上的一块区域，因此其访问速度比物理内存慢。</li>
<li>Android基于Linux内核，两者主要差别在于Android系统没有交换空间(Swap space)</li>
<li>于是Android系统引入了OOM( Out Of Memory ) Killer 来解决内存资源被耗尽的问题。</li>
<li>其作用是根据进程所消耗的内存大小以及进程的“visibility state”来决定是否杀死这个进程，从而达到释放内存的目的。</li>
<li>Activity Manager会给不同状态下的进程设置相对应的oom_adj 值：</li>
</ul>
<pre><code class="copyable"># Define the oom_adj values for the classes of processes that can be
# killed by the kernel.  These are used in ActivityManagerService.
    setprop ro.FOREGROUND_APP_ADJ 0    //前台进程
    setprop ro.VISIBLE_APP_ADJ 1       //可见进程
    setprop ro.SECONDARY_SERVER_ADJ 2  //次要服务
    setprop ro.BACKUP_APP_ADJ 2        //备份进程
    setprop ro.HOME_APP_ADJ 4          //桌面进程
    setprop ro.HIDDEN_APP_MIN_ADJ 7    //后台进程
    setprop ro.CONTENT_PROVIDER_ADJ 14 //内容供应节点
    setprop ro.EMPTY_APP_ADJ 15        //空进程
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>因此，1是应用占用内存越少，越可能存活下去；2是要合理设计后台任务进程</li>
</ul>
<h4 data-id="heading-1">后台任务</h4>
<ul>
<li>Android开发基本都会用到后台任务，通常是不需要用户感知的耗时功能，任务完成后需要及时关闭任务回收资源，若使用不合理则可能造成电量大量消耗；</li>
<li>之前我们处理后台任务一般使用service或线程池，尤其是service又不受Activity生命周期影响，被广泛用于数据缓存，统计及日志上传，消息推送，环境监听，进程保活拉起等，如此过于滥用给用户带来耗电快，被打扰，隱私泄露等问题，于是google在新的Android版本中逐渐增加限制，Doze机制，app Standby等，尤其是Android8.0不允许创建后台服务，无法在清单文件中注册隐式广播接收器; 所以我们所熟知的Servcie已经被弃用了，因为它不再被允许在后台执行长时间的操作，即便这是它最初被设计出来的目的, 除了ForegroundService之外，我们已经没有任何理由再去使用Service了；</li>
</ul>
<h4 data-id="heading-2">Google推荐的不同场景后台任务的处理方案</h4>
<ol>
<li>需系统触发，不必完成：ThreadPool + Broadcast</li>
<li>需系统触发，必须完成，可推迟：WorkManager</li>
<li>需系统触发，必须完成，立即：ForegroundService + Broadcast</li>
<li>不需系统触发，不必完成：ThreadPool</li>
<li>不需系统触发，必须完成，可推迟：WorkManager</li>
<li>不需系统触发，必须完成，立即：ForegroundService</li>
</ol>
<h3 data-id="heading-3">WorkManager简介</h3>
<ul>
<li>一个可兼容，灵活，简单的延迟后台任务；</li>
<li>能根据系统版本，选择不同实现方案，API高于23时采用JobScheduler，以帮助优化电池寿命和批处理作业，而在6.0以下系统版本则可自动切换为AlarmManager+Broadcast Receiver，最终都是交由Executor来执行；</li>
</ul>
<h3 data-id="heading-4">WorkManager优点</h3>
<ul>
<li>兼容性：兼容到api14</li>
<li>可指定约束条件：如有网络才执行</li>
<li>可指定执行次数和定时</li>
<li>多个任务可使用任务链</li>
<li>保证执行：如当前不满足或app挂掉后，下次满足条件再执行</li>
<li>支持省电模式</li>
</ul>
<h3 data-id="heading-5">WorkManager使用</h3>
<h5 data-id="heading-6">导入依赖</h5>
<pre><code class="copyable">implementation "androidx.work:work-runtime-ktx:2.5.0"
// optional - RxJava2 support
implementation "androidx.work:work-rxjava2:2.5.0"
// optional - Test helpers
androidTestImplementation "androidx.work:work-testing:2.5.0"
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">自定义Worker</h5>
<ul>
<li>谷歌提供了四种Worker给我们使用，分别为：
<ul>
<li>自动运行在后台线程的Worker</li>
<li>结合协程的CoroutineWorker</li>
<li>结合RxJava2的RxWorker</li>
<li>以上三个类的基类的ListenableWorker</li>
</ul>
</li>
<li>我使用的是CoroutineWorker，然后重写doWork方法，其代码如下</li>
</ul>
<pre><code class="copyable">class MyWorker(appContext: Context, workerParameters: WorkerParameters) :
    CoroutineWorker(appContext, workerParameters) &#123;

    //执行在一个单独的后台线程里
    override suspend fun doWork(): Result &#123;
        LjyLogUtil.d("doWork start")
        delay(5000)//模拟处理任务耗时
        LjyLogUtil.d("doWork end")
        return Result.success()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>doWork方法执行在一个单独的后台线程里</li>
<li>doWork的结果有三种，分别为：
<ul>
<li>Result.success()：工作成功完成。</li>
<li>Result.failure()：工作失败。</li>
<li>Result.retry()：工作失败，根据其重试政策在其他时间尝试。</li>
</ul>
</li>
</ul>
<h5 data-id="heading-8">执行单次任务</h5>
<ul>
<li>单次任务使用OneTimeWorkRequestBuilder创建workRequest，再通过WorkManager对象的enqueue()方法将其提交到WorkManager</li>
</ul>
<pre><code class="copyable">class WorkManagerActivity : AppCompatActivity() &#123;
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_work_manager)
        //执行单次任务
        val workRequest = OneTimeWorkRequestBuilder<MyWorker>().build()
        WorkManager.getInstance(this).enqueue(workRequest)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">定期循环任务</h5>
<ul>
<li>可用于如定期上传日志，定期缓存预加载的数据，定期备份等</li>
<li>使用PeriodicWorkRequest.Builder创建workRequest</li>
</ul>
<pre><code class="copyable">val workRequest2 =
            PeriodicWorkRequest.Builder(MyWorker::class.java, 3, TimeUnit.SECONDS).build()
WorkManager.getInstance(this).enqueue(workRequest2)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>还可以定义具有灵活时间段的定期工作，如在每小时的最后 15 分钟内运行定期工作</li>
</ul>
<pre><code class="copyable">val workRequest2: WorkRequest = PeriodicWorkRequest.Builder(
        MyWorker::class.java,
        1, TimeUnit.HOURS,
        15, TimeUnit.MINUTES
    ).build()
WorkManager.getInstance(this).enqueue(workRequest2)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">设置任务约束条件</h5>
<ul>
<li>如果不满足某个约束,WorkManager将停止工作，并且系统将在满足所有约束后重试工作</li>
</ul>
<pre><code class="copyable">val constraints = Constraints.Builder()
            //设备空闲状态时运行
            .setRequiresDeviceIdle(true)
            //特定的网络状态运行
            //NOT_REQUIRED不需要网络
            //CONNECTED任何可用网络
            //UNMETERED需要不计量网络，如WiFi
            //NOT_ROAMING需要非漫游网络
            //METERED需要计量网络，如4G
            .setRequiredNetworkType(NetworkType.CONNECTED)
            //电量充足时运行
            .setRequiresBatteryNotLow(true)
            //充电时执行
            .setRequiresCharging(true)
            //存储空间足够时运行
            .setRequiresStorageNotLow(true)
            //指定是否在(Uri指定的)内容更新时执行本次任务
            .addContentUriTrigger(Uri.EMPTY, true)
            .build()
val workRequest = OneTimeWorkRequestBuilder<MyWorker>()
        .setConstraints(constraints)
        .build()
WorkManager.getInstance(this).enqueue(workRequest)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">分配输入数据</h5>
<pre><code class="copyable">//1. 传入数据
val inputData = Data.Builder().putString("name", "ljy").build()
val workRequest = OneTimeWorkRequestBuilder<MyWorker>()
        .setInputData(inputData)
        .build()
WorkManager.getInstance(this).enqueue(workRequest)
//2.接收数据
class MyWorker(appContext: Context, workerParameters: WorkerParameters) :
        CoroutineWorker(appContext, workerParameters) &#123;
    override suspend fun doWork(): Result &#123;
        val name = inputData.getString("name")
        LjyLogUtil.d("doWork start:name=$name")
        delay(5000)
        LjyLogUtil.d("doWork end")
        return Result.success()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">延时执行</h5>
<pre><code class="copyable">val workRequest = OneTimeWorkRequestBuilder<MyWorker>()
        .setInitialDelay(1, TimeUnit.SECONDS)
        .build()
WorkManager.getInstance(this).enqueue(workRequest)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">设置tag</h5>
<ul>
<li>可以用于取消工作或观察其进度,或者对任务进行分组</li>
<li>如果有一组在逻辑上相关的工作，对这些工作项进行标记可能也会很有帮助</li>
</ul>
<pre><code class="copyable">val workRequest = OneTimeWorkRequestBuilder<MyWorker>()
        .addTag("myWorker")
        .build()
WorkManager.getInstance(this).enqueue(workRequest)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">重试和退避政策</h5>
<ul>
<li>工作器返回 Result.retry()，系统将根据退避延迟时间和退避政策重新调度工作;</li>
<li>退避延迟时间:指定了首次尝试后重试工作前的最短等待时间;</li>
<li>退避政策: 定义了在后续重试过程中，退避延迟时间随时间以怎样的方式增长,WorkManager 支持 2 个退避政策，即 LINEAR 和 EXPONENTIAL;</li>
<li>每个工作请求都有退避政策和退避延迟时间, 默认政策是 EXPONENTIAL，延迟时间为 10 秒，开发者可以在工作请求配置中替换此默认设置。</li>
</ul>
<pre><code class="copyable">val workRequest4: WorkRequest = OneTimeWorkRequest.Builder(MyWorker::class.java)
    .setBackoffCriteria(
        BackoffPolicy.LINEAR,
        OneTimeWorkRequest.MIN_BACKOFF_MILLIS,
        TimeUnit.MILLISECONDS
    )
    .build()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">创建任务链</h5>
<ul>
<li>例如先执行任务1，再执行任务2和任务5，任务2执行完后执行任务3，任务4</li>
</ul>
<pre><code class="copyable">val request1 = OneTimeWorkRequest.Builder(MyWorker::class.java).build()
val request2 = OneTimeWorkRequest.Builder(MyWorker::class.java).build()
val request3 = OneTimeWorkRequest.Builder(MyWorker::class.java).build()
val request4 = OneTimeWorkRequest.Builder(MyWorker::class.java).build()
val request5 = OneTimeWorkRequest.Builder(MyWorker::class.java).build()
val workConstraints = WorkManager.getInstance(this).beginWith(request1)
workConstraints.then(request2).then(listOf(request3, request4)).enqueue()
workConstraints.then(request5).enqueue()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">唯一链</h5>
<ul>
<li>同一时间内队列里不能存在相同名称的任务
<ul>
<li>WorkManager.enqueueUniqueWork()：用于一次性工作</li>
<li>WorkManager.enqueueUniquePeriodicWork()：用于定期工作</li>
</ul>
</li>
<li>应用场景：多次请求接口数据，如下单，更换头像等</li>
<li>例如替换头像要经历本地文件读取，压缩，上传三个任务，下面组成一个串行的任务连，并且设置唯一标识，则代码如下：</li>
</ul>
<pre><code class="copyable">val requestLoadFromFile = OneTimeWorkRequest.Builder(MyWorker::class.java).build()
val requestZip = OneTimeWorkRequest.Builder(MyWorker::class.java)
    .setInputData(createInputDataForUri()).build()
val requestSubmitToService = OneTimeWorkRequest.Builder(MyWorker::class.java).build()
WorkManager.getInstance(this).beginUniqueWork(
    "tagChangeImageHeader",
    ExistingWorkPolicy.REPLACE,
    requestLoadFromFile
)
    .then(requestZip)
    .then(requestSubmitToService)
    .enqueue()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>其中参数existingWorkPolicy有三种可选：
<ul>
<li>REPLACE：若相同，删除已有的任务，添加现有的任务；</li>
<li>KEEP：若相同，让已有的继续执行，不添加新任务；</li>
<li>APPEND：若相同，则添加新任务到已有任务链最末端；</li>
</ul>
</li>
</ul>
<h5 data-id="heading-17">Work状态</h5>
<ul>
<li>当WorkManager把任务加入队列后，会为每个WorkRequest对象提供一个LiveData;</li>
<li>LiveData持有WorkStatus,通过观察该 LiveData, 我们可以确定任务的当前状态, 并在任务完成后获取所有返回的值；</li>
</ul>
<pre><code class="copyable">ENQUEUED,//已加入队列
RUNNING,//运行中
SUCCEEDED,//已成功
FAILED,//已失败
BLOCKED,//已挂起
CANCELLED;//已取消
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>状态的更改分为一次性任务的状态和周期性任务的状态:
<ul>
<li>一次性任务状态：初始状态为 ENQUEUED，在满足其 Constraints 和初始延迟计时要求后立即运行，转为 RUNNING,
根据工作的结果转为 SUCCEEDED、FAILED 状态, 如果结果是Result.retry() ,它可能会回到 ENQUEUED 状态;
SUCCEEDED、FAILED 和 CANCELLED 均表示此工作的终止状态,WorkInfo.State.isFinished() 都将返回 true;
在此过程中，随时都可以取消工作，取消后工作将进入 CANCELLED 状态;</li>
<li>定期任务状态：因为是循环执行的，所以终止状态只有一个CANCELLED，其他和一次性任务状态是一样;</li>
</ul>
</li>
</ul>
<h6 data-id="heading-18">状态监听</h6>
<pre><code class="copyable">// by id
WorkManager.getInstance(this).getWorkInfoById(request1.id)
WorkManager.getInstance(this).getWorkInfoByIdLiveData(request1.id)
// by name
WorkManager.getInstance(this).getWorkInfosForUniqueWork("sync");
WorkManager.getInstance(this).getWorkInfosForUniqueWorkLiveData("sync");
// by tag
WorkManager.getInstance(this).getWorkInfosByTag("syncTag")
WorkManager.getInstance(this).getWorkInfosByTagLiveData("syncTag")
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-19">WorkQuery</h6>
<ul>
<li>WorkManager 2.4.0 及更高版本还支持使用 WorkQuery 对象对已加入队列的作业进行复杂查询，</li>
<li>WorkQuery 支持按工作的标记、状态和唯一工作名称的组合进行查询</li>
</ul>
<pre><code class="copyable">val workQuery = WorkQuery.Builder
    .fromTags(listOf("syncTag"))
    .addStates(listOf(WorkInfo.State.FAILED, WorkInfo.State.CANCELLED))
    .addUniqueWorkNames(
        listOf("preProcess", "sync")
    )
    .build()
val workInfos: ListenableFuture<List<WorkInfo>> =
    WorkManager.getInstance(this).getWorkInfos(workQuery)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">更新进度 和 观察进度</h5>
<ul>
<li>Java: 使用Worker.setProgressAsync()更新进度</li>
<li>Kotlin：使用 CoroutineWorker.setProgress()更新进度，代码如下</li>
</ul>
<pre><code class="copyable">class MyWorker(appContext: Context, workerParameters: WorkerParameters) :
        CoroutineWorker(appContext, workerParameters) &#123;
        
    override suspend fun doWork(): Result &#123;
        val name = inputData.getString("name")
        LjyLogUtil.d("doWork start:name=$name")
        val p0 = workDataOf("progressValue" to 0)
        val p1 = workDataOf("progressValue" to 20)
        val p2 = workDataOf("progressValue" to 40)
        val p3 = workDataOf("progressValue" to 60)
        val p4 = workDataOf("progressValue" to 80)
        val p5 = workDataOf("progressValue" to 100)
        setProgress(p0)
        delay(1000)
        setProgress(p1)
        delay(1000)
        setProgress(p2)
        delay(1000)
        setProgress(p3)
        delay(1000)
        setProgress(p4)
        delay(1000)
        setProgress(p5)
        LjyLogUtil.d("doWork end")
        return Result.success()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>观察进度：和上面的监听任务状态是一样的，使用 getWorkInfoBy…() 或 getWorkInfoBy…LiveData(),代码如下</li>
</ul>
<pre><code class="copyable">val workRequest10 = OneTimeWorkRequestBuilder<MyWorker>().build()
WorkManager.getInstance(this).enqueue(workRequest10)
WorkManager.getInstance(this)
    .getWorkInfoByIdLiveData(workRequest10.id)
    .observe(this, &#123;
        if (it != null) &#123;
            LjyLogUtil.d("workRequest10:state=$&#123;it.state&#125;")
            val progress = it.progress;
            val value = progress.getInt("progressValue", 0)
            LjyLogUtil.d("workRequest10:progress=$value")
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">取消任务</h5>
<pre><code class="copyable">//取消所有任务
WorkManager.getInstance(this).cancelAllWork()
//取消一组带有相同标签的任务
WorkManager.getInstance(this).cancelAllWorkByTag("tagName")
//根据name取消任务
WorkManager.getInstance(this).cancelUniqueWork("uniqueWorkName")
//根据id取消任务
WorkManager.getInstance(this).cancelWorkById(workRequest.id)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">任务停止</h5>
<ul>
<li>正在运行的任务可能因为某些原因而停止运行，主要的原因有以下一些：</li>
</ul>
<pre><code class="copyable">1. 明确要求取消它，可以调用WorkManager.cancelWorkById(UUID)方法。
2. 如果是唯一任务，将 ExistingWorkPolicy 为 REPLACE 的新 WorkRequest 加入到了队列中时，旧的 WorkRequest 会立即被视为已取消。
3. 添加的任务约束条件不再适合。
4. 系统出于某种原因指示应用停止工作。
5. 当任务停止后，WorkManager 会立即调用 ListenableWorker.onStopped()关闭可能保留的所有资源。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">我是今阳，如果想要进阶和了解更多的干货，欢迎关注微信公众号 “今阳说” 接收我的最新文章</h3></div>  
</div>
            