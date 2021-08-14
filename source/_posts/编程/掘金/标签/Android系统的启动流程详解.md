
---
title: 'Android系统的启动流程详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=990'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 18:25:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=990'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“<strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<h1 data-id="heading-0">Android系统启动流程.</h1>
<h4 data-id="heading-1">1.当系统引导程序启动Linux内核时, 内核会加载各种数据结构和驱动程序. 有了驱动之后, 开始启动Android系统并加载用户级别的第一个进程init(system/core/init/Init.c).</h4>
<pre><code class="copyable">    int main(int argc, char **argv)
    &#123;
        ...

        // 创建各种文件夹和挂载目录.
        mkdir("/dev", 0755);

        ...

        // 初始化日志.
        log_init();

        // 解析配置文件.
        init_parse_config_file("/init.rc");

        ...

        return 0;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">2.加载Init.rc文件. 主要启动了一个Zygote(孵化器)进程, 此进程是Android系统启动关键服务的一个母进程.</h4>
<pre><code class="copyable">    service zygote /system/bin/app_process -Xzygote /system/bin --zygote --start-system-server
        socket zygote stream 666
        onrestart write /sys/android_power/request_state wake
        onrestart write /sys/power/state on
        onrestart restart media
        onrestart restart netd
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">3.Zygote进程的初始化在App_main.cpp文件中开启, 代码片段如下:</h4>
<pre><code class="copyable">int main(int argc, const char* const argv[])
&#123;
    // 定义Android运行时环境.
    AppRuntime runtime;
    int i = runtime.addVmArguments(argc, argv);

    ...

    bool startSystemServer = (i < argc) ? 
            strcmp(argv[i], "--start-system-server") == 0 : false;
    setArgv0(argv0, "zygote");
    set_process_name("zygote");

    // 使用运行时环境启动Zygote的初始化类.
    runtime.start("com.android.internal.os.ZygoteInit",
        startSystemServer);

    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">4.现在从c或c++代码进入到java代码中, ZygoteInit.java初始化类, 代码如下:</h4>
<pre><code class="copyable">    public static void main(String argv[]) &#123;
        // 加载系统运行依赖的class类.
        preloadClasses();

        ...

        if (argv[1].equals("true")) &#123;
            // Zygote孵化器进程开始孵化系统核心服务.
            startSystemServer();
        &#125; else if (!argv[1].equals("false")) &#123;
            throw new RuntimeException(argv[0] + USAGE_STRING);
        &#125;

        ...
    &#125;

    private static boolean startSystemServer()
        throws MethodAndArgsCaller, RuntimeException &#123;
        String args[] = &#123;
            "--setuid=1000",
            "--setgid=1000",
            "--setgroups=1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,3001,3002,3003",
            "--capabilities=130104352,130104352",
            "--runtime-init",
            "--nice-name=system_server",
            "com.android.server.SystemServer",
        &#125;;

        ...

        // 孵化器分叉开启SystemServer类, 并且把上面定义的参数.
        // 传递给此类. 用于启动系统关键服务.
        pid = Zygote.forkSystemServer(
                parsedArgs.uid, parsedArgs.gid,
                parsedArgs.gids, debugFlags, null,
                parsedArgs.permittedCapabilities,
                parsedArgs.effectiveCapabilities);

        ...
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">5.Zygote进程分叉出SystemServer类, main函数如下:</h4>
<pre><code class="copyable">    public static void main(String[] args) &#123;
        ...

        // 加载本地的动态链接库.
        System.loadLibrary("android_servers");

        // 调用动态链接库中的c函数.
        init1(args);
    &#125;

    // 这里init1的函数定义在frameworks\base\services\jni\com_android_server_SystemServer.cpp下的方法.
    native public static void init1(String[] args);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">6.com<em>android</em>server_SystemServer.cpp的代码片段如下:</h4>
<pre><code class="copyable">    static JNINativeMethod gMethods[] = &#123;
        /* name, signature, funcPtr */
        // 把native方法init1, 映射到android_server_SystemServer_init1. (这里是定义的函数指针)
        &#123; "init1", "([Ljava/lang/String;)V", (void*) android_server_SystemServer_init1 &#125;,
    &#125;;

    static void android_server_SystemServer_init1(JNIEnv* env, jobject clazz)
    &#123;
        // 转调
        system_init();
    &#125;

    // 此方法没有方法体.
    extern "C" int system_init();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">7.system_init方法的方法体, 在System_init.cpp类中. 代码如下:</h4>
<pre><code class="copyable">    extern "C" status_t system_init()
    &#123;
        ...

        // 开启一些硬件相关的服务.
        SensorService::instantiate();

        ...

        // 获取Android运行时环境
        AndroidRuntime* runtime = AndroidRuntime::getRuntime();

        LOGI("System server: starting Android services.\n");
        // 调用SystemServer类中静态方法init2. 从native层转到java层.
        runtime->callStatic("com/android/server/SystemServer", "init2");

        ...
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">8.SystemServer下init2方法如下:</h4>
<pre><code class="copyable">    public static final void init2() &#123;
        Slog.i(TAG, "Entered the Android system server!");

        // 进入Android系统服务的初始化.
        Thread thr = new ServerThread();
        thr.setName("android.server.ServerThread");
        thr.start();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">9.ServerThread中的run方法如下:</h4>
<pre><code class="copyable">    @Override
    public void run() &#123;
        ...

        // 初始化系统的服务, 并且把服务添加ServiceManager中, 便于以后系统进行统一管理.
        ServiceManager.addService("entropy", new EntropyService());

        ...

        // 调用了ActivityManagerService的systemReady的方法.
        ((ActivityManagerService)ActivityManagerNative.getDefault())
                .systemReady(new Runnable() &#123;
            public void run() &#123;
                ...
            &#125;
        &#125;);

        ...
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">10.ActivityManagerService下的systemReady方法如下:</h4>
<pre><code class="copyable">public void systemReady(final Runnable goingCallback) &#123;
    ...

    // 调用了ActivityStack中的resumeTopActivityLocked去启动Activity
    mMainStack.resumeTopActivityLocked(null);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">11.ActivityStack中的resumeTopActivityLocked方法如下:</h4>
<pre><code class="copyable">    final boolean resumeTopActivityLocked(ActivityRecord prev) &#123;
            // 找到第一个当前没有关闭的Activity, 系统刚刚系统没有任何Activity执行, 所以next为null
            ActivityRecord next = topRunningActivityLocked(null);

            // Remember how we'll process this pause/resume situation, and ensure
            // that the state is reset however we wind up proceeding.
            final boolean userLeaving = mUserLeaving;
            mUserLeaving = false;

            if (next == null) &#123;
                // There are no more activities!  Let's just start up the
                // Launcher...
                if (mMainStack) &#123;
                    // 开启Launcher应用的第一个Activity界面.
                    return mService.startHomeActivityLocked();
                &#125;
            &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">12.home界面显示, 这时Android系统启动完毕. 进入到待机画面.</h4></div>  
</div>
            