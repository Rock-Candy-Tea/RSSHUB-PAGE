
---
title: 'Android架构师之路_JNI与NDK编程常用方法史上最全总结和详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6eb76d69a38e47c494447d74431fe771~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:03:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6eb76d69a38e47c494447d74431fe771~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>前沿小计</strong></p>
<p>1、前面把JNI与NDK编程基础知识点总结过了，如果不懂的可以再详细看下；</p>
<p>2、今天讲解下jni编程中常用的方法总结和详解-中文的：类操作方法、字符串、数组、方法等等；</p>
<p>3、jni编程一定要会的，不懂的就问；</p>
<p><strong>一、JNI中重要的JavaVM 和 JNIEnv详解</strong></p>
<p><strong><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6eb76d69a38e47c494447d74431fe771~tplv-k3u1fbpfcp-zoom-1.image" alt="Dingtalk_20210722141216.jpg" loading="lazy" referrerpolicy="no-referrer"></strong></p>
<p>JNI 定义了两个关键数据结构，即JavaVM和JNIEnv。两者本质上都是指向函数表的二级指针。在 C++ 版本中，它们是一些类，这些类具有指向函数表的指针，并具有每个通过该函数表间接调用的 JNI 函数的成员函数</p>
<p><strong>1. JavaVM</strong></p>
<p>JavaVM是虚拟机在JNI中的表示，一个JVM中只有一个JavaVM对象，这个对象是线程共享的。</p>
<p>通过JNIEnv我们可以获取一个Java虚拟机对象，其函数如下：</p>
<p>/**</p>
<p>* 获取Java虚拟机对象</p>
<p>* @param env JNIEnv对象</p>
<p>* @param vm 用来存放获得的虚拟机的指针的指针</p>
<p>* @return 成功返回0，失败返回其他</p>
<p>*/</p>
<p>jint GetJavaVM(JNIEnv *env, JavaVM **vm);</p>
<p>在加载动态链接库的时候，JVM会调用JNI_OnLoad(JavaVM* jvm, void* reserved)（如果定义了该函数），第一个参数会传入JavaVM指针。可以在该函数中保存JavaVM指针来供全局使用。</p>
<p>JavaVM *javaVM = NULL;</p>
<p>jint JNI_OnLoad(JavaVM *vm, void *reserved) &#123;</p>
<p>javaVM = vm;</p>
<p>...</p>
<p>&#125;</p>
<p><strong>2. JNIEnv</strong></p>
<p>JNIEnv类型是一个指向全部JNI方法的指针，JNIEnv 提供了大部分 JNI 函数。JNIEnv只在创建它的线程有效，不能跨线程传递，不能再线程之间共享 JNIEnv。</p>
<p>所有的本地接口函数都会以 JNIEnv 作为第一个参数。不管是静态注册的本地C/C++函数接口，还是动态注册的本地函数接口，函数的第一个参数都是JNIEnv。</p>
<p>静态注册的函数实例</p>
<p>JNIEXPORT jstring JNICALL Java_cc_ccbu_jnitest_Test</p>
<p>(JNIEnv *, jobject) &#123;</p>
<p>return env->NewStringUTF("test");</p>
<p>&#125;</p>
<p>动态注册的函数实例</p>
<p>jstring testtest(JNIEnv* env, jobject thiz) &#123;</p>
<p>return env->NewStringUTF("test");</p>
<p>&#125;</p>
<p>static JNINativeMethod gMethods[] = &#123;</p>
<p>&#123;"testtest", "()Ljava/lang/String;", (void*)testtest&#125;</p>
<p>&#125;;</p>
<p>int registerMethod(JNIEnv *env) &#123;</p>
<p>jclass test = env->FindClass("cc/ccbu/jnitest/Test");</p>
<p>return env->RegisterNatives(test, gMethods, sizeof(gMethods)/ sizeof(gMethods[0]));</p>
<p>&#125;</p>
<p>如果一段代码无法通过其他方法获取自己的 JNIEnv，可以通过全局有效的 JavaVM，然后使用 GetEnv 来获取当前线程的 JNIEnv（如果该线程包含一个 JNIEnv）。</p>
<p>JNIEnv* env = NULL;</p>
<p>if (javaVM->GetEnv((void**) &env, JNI_VERSION_1_6) != JNI_OK) &#123;</p>
<p>return JNI_ERR;</p>
<p>&#125;</p>
<p>GetEnv函数定义如下：</p>
<p>/**</p>
<p>* 获取当前线程JNIEnv</p>
<p>* @param env 用来存放获取JNIEnv对象的指针的指针</p>
<p>* @param version JNI版本</p>
<p>* @return 成功返回0，失败返回其他</p>
<p>*/</p>
<p>jint GetEnv(void** env, jint version)</p>
<p>对于本地库中创建的线程，需要使用AttachCurrentThread来附加到 JavaVM来获取一个可用的JNIEnv。线程退出或不再需要使用JNIEnv时，必须通过调用DetachCurrentThread来解除连接。</p>
<p>JNIEnv *env = NULL;</p>
<p>JavaVM *vm = cachedVM;</p>
<p>bool bAttached = AttachCurrentThread(vm, &env);</p>
<p>if(bAttached) &#123;</p>
<p>vm->DetachCurrentThread();</p>
<p>&#125;</p>
<p>bool AttachCurrentThread(JavaVM* vm, JNIEnv** p_env)</p>
<p>&#123;</p>
<p>bool bAttached = false;</p>
<p>switch(vm->GetEnv((void**)p_env, JNI_VERSION_1_4))</p>
<p>&#123;</p>
<p>case JNI_OK:</p>
<p>break;</p>
<p>case JNI_EDETACHED:</p>
<p>if (vm->AttachCurrentThread(p_env, 0) < 0)</p>
<p>&#123;</p>
<p>LOGD("%s :Attached failed!",__func__);</p>
<p>return false;</p>
<p>&#125;</p>
<p>else</p>
<p>&#123;</p>
<p>bAttached = true;</p>
<p>&#125;</p>
<p>break;</p>
<p>case JNI_EVERSION:</p>
<p>LOGE("Invalid java version");</p>
<p>break;</p>
<p>&#125;</p>
<p>return bAttached;</p>
<p>&#125;</p>
<p><strong>二、jni的接口函数表</strong></p>
<p><strong><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d526b1c15d7b45598cb144ad40214262~tplv-k3u1fbpfcp-zoom-1.image" alt="5713484-489382d33286e74e.png" loading="lazy" referrerpolicy="no-referrer"></strong></p>
<p>每个函数都可以通过JNIEnv参数访问，JNIEnv类型是指向一个存放所有JNI接口指针的指针，其定义如下：</p>
<p>typedef const struct JNINativeInterface *JNIEnv;</p>
<p>虚拟机初始化函数表，如下面代码所示，前三个条目是为了将来和COM兼容而保留的。另外，我们在函数表的开头附近保留了一些额外的NULL条目，例如，可以在FindClass之后添加未来与类相关的JNI操作，而不是在表的末尾。请注意，函数表可以在所有JNI接口指针之间共享。</p>
<p>首先我们来看下JNINativeInterface</p>
<p>const struct JNINativeInterface ... = &#123;</p>
<p>GetVersion,</p>
<p>DefineClass,</p>
<p>FindClass,</p>
<p>FromReflectedMethod,</p>
<p>FromReflectedField,</p>
<p>ToReflectedMethod,</p>
<p>GetSuperclass,</p>
<p>IsAssignableFrom,</p>
<p>ToReflectedField,</p>
<p>Throw,</p>
<p>ThrowNew,</p>
<p>ExceptionOccurred,</p>
<p>ExceptionDescribe,</p>
<p>ExceptionClear,</p>
<p>FatalError,</p>
<p>PushLocalFrame,</p>
<p>PopLocalFrame,</p>
<p>NewGlobalRef,</p>
<p>DeleteGlobalRef,</p>
<p>DeleteLocalRef,</p>
<p>IsSameObject,</p>
<p>NewLocalRef,</p>
<p>EnsureLocalCapacity,</p>
<p>AllocObject,</p>
<p>NewObject,</p>
<p>NewObjectV,</p>
<p>NewObjectA,</p>
<p>GetObjectClass,</p>
<p>IsInstanceOf,</p>
<p>...</p>
<p>...</p>
<p>...</p>
<p>...</p>
<p>&#125;;</p>
<p><strong>三、获取JNI版本信息</strong></p>
<p>在JNIEnv指针中，有个函数用于获取JNI的版本：</p>
<p>jint GetVersion(JNIEnv *env);</p>
<p>该方法主要返回本地JNI方法接口的版本信息。在不同的JDK环境下返回值是不同的，具体如下：</p>
<p>在JDK/JRE 1.1中，返回0x00010001</p>
<p>在JDK/JRE 1.2中，返回0x00010002</p>
<p>在JDK/JRE 1.3中，返回0x00010004</p>
<p>在JDK/JRE 1.4中，返回0x00010006</p>
<p>上面这些数字可不是我乱拍的，其实是早就被定义为一个宏了，如下：</p>
<p>#define JNI_VERSION_1_1 0x00010001</p>
<p>#define JNI_VERSION_1_2 0x00010002</p>
<p>/* Error codes */</p>
<p>#define JNI_EDETACHED (-2) /* thread detached from the VM */</p>
<p>#define JNI_EVERSION (-3) /* JNI version error</p>
<p>SINCE JDK/JRE 1.4:</p>
<p>#define JNI_VERSION_1_4 0x00010004</p>
<p>SINCE JDK/JRE 1.6:</p>
<p>#define JNI_VERSION_1_6 0x00010006</p>
<p><strong>四、Java 类 操作</strong></p>
<p><strong>(一)、定义类(加载类)</strong></p>
<p>jclass DefineClass(JNIEnv *env,const char* name,jobject loader,const jbyte *buf, jsize bufLen)</p>
<p>这个函数，主要是从包含数据的buffer中加载类，该buffer包含类调用时未被虚拟机所引用的原始类数据。</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p>name：所定义的类名或者接口名，该字符串有modefied UTF-8编码</p>
<p>loader：指派给定义的类加载器</p>
<p>buf：包含.class文件数据的buffer</p>
<p>bufLen：buffer长度</p>
<p>返回：Java类对象，当错误出现时返回NULL</p>
<p>可能抛出的异常：</p>
<p>如果没有指定这个Java类的，则会抛出ClassFormatError</p>
<p>如果是一个类/接口是它自己的一个父类/父接口，则会抛出ClassCircularityError</p>
<p>如果内存不足，则会抛出OutOfMemoryError</p>
<p>如果想尝试在Java包中定义一个类，则会抛出SecurityException</p>
<p><strong>(二)、查找类</strong></p>
<p>jclass FindClass(JNIEnv *env,const char *name);</p>
<p>这里面有两种情况一个是JDK release1.1，另外一种是JDK release 1.2</p>
<p>。从JDK release 1.1，该函数加载一个本地定义类，它搜索CLASSPATH环境变量里的目录及zip文件查找特定名字的类。自从Java 2 release 1.2，Java安全模型允许非系统类加载跟调用本地方法。FindClass定义与当前本地方法关联的类加载，也就是声明本地方法的类的类加载类。如果本地方法属于系统类，则不会涉及类加载器；否则，将调用适当的类加载来加载和链接指定的类。从Java 2 SDK1.2版本开始，通过调用接口调用FindClass时，没有当前的本机方法或关联的的类加载器。在这种情况下，在这种情况下，使用ClassLoader.getSystemClassLoader的结果。这是虚拟机为应用程序创建的类加载器，并且能够找到java.class.path属性列出的类。</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p>name：一个完全限定的类名，即包含“包名”+“/”+类名。举个例子：如java.lang.String，该参数为java/lang/String；如果类名以[开头，将返回一个数组类。比如数组类的签名为java.lang.Object[]，该参数应该为"[Ljava/lang/Object"</p>
<p>返回：</p>
<p>返回对应完全限定类对象，当找不到类时，返回NULL</p>
<p>可能抛出的异常：</p>
<p>如果没有指定这个Java类的，则会抛出ClassFormatError</p>
<p>如果是一个类/接口是它自己的一个父类/父接口，则会抛出ClassCircularityError</p>
<p>如果没有找到该类/接口的定义，则抛出NoClassDefFoundError</p>
<p>如果内存不足，则会抛出OutOfMemoryError</p>
<p><strong>(三)、查找父类</strong></p>
<p>jclass GetSuperclass(JNIEnv *env,jclass clazz);</p>
<p>如果clazz不是Object类，则此函数将返回表示该clazz的父类的Class对象，如果该类是Object，或者clazz代表接口，则此函数返回NULL。</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：Java的Class类</p>
<p>返回：</p>
<p>如果clazz有父类则返回其父类，如果没有其父类则返回NULL</p>
<p><strong>(四)、安全转换</strong></p>
<p>jboolean IsAssignableFrom(JNIEnv *env,jclass clazz1,jclass clazz2);</p>
<p>判断clazz1的对象是否可以安全地转化为clazz2的对象</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p>clazz1：Java的Class类，即需要被转化的类</p>
<p>clazz2：Java的Class类，即需要转化为目标的类</p>
<p>返回：</p>
<p>如果满足以下任一条件，则返回JNI_TRUE：</p>
<p>如果clazz1和clazz2是同一个Java类。</p>
<p>如果clazz1是clazz2的子类</p>
<p>如果clazz1是clazz2接口的实现类</p>
<p><strong>四、异常 操作</strong></p>
<p><strong>(一)、抛出异常</strong></p>
<p>jint Throw(JNIEnv *env,jthrowable obj);</p>
<p>传入一个jthrowable对象，并且在JNI并将其抛起</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p>jthrowable：一个Java的java.lang.Throwable对象</p>
<p>返回：</p>
<p>成功返回0，失败返回一个负数。</p>
<p>可能抛出的异常：</p>
<p>抛出一个java.lang.Throwable 对象</p>
<p><strong>(二)、构造一个新的异常并抛出</strong></p>
<p>jint ThrowNew(JNIEnv *env,jclass clazz,const char* message);</p>
<p>传入一个message，并用其构造一个异常并且抛出。</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p>jthrowable：一个Java的java.lang.Throwable对象</p>
<p>message：用于构造一个java.lang.Throwable对象的消息，该字符串用modified UTF-8编码</p>
<p>返回：</p>
<p>如果成功返回0，失败返回一个负数</p>
<p>可能抛出的异常：</p>
<p>抛出一个新构造的java.lang.Throwable 对象</p>
<p><strong>(三)、检查是否发生异常，并抛出异常</strong></p>
<p>jthrowable ExceptionOccurred(JNIEnv *env);</p>
<p>检测是否发生了异常，如果发生了，则返回该异常的引用(再调用ExceptionClear()函数前，或者Java处理异常前)，如果没有发生异常，则返回NULL。</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p>返回：</p>
<p>jthrowable的异常引用或者NULL</p>
<p><strong>(四)、打印异常的堆栈信息</strong></p>
<p>void ExceptionDescribe(JNIEnv *env)</p>
<p>打印这个异常的堆栈信息</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p><strong>(五)、清除异常的堆栈信息</strong></p>
<p>void ExceptionClear(JNIEnv *env);</p>
<p>清除正在抛出的异常，如果当前没有异常被抛出，这个函数不起作用</p>
<p>入参解释：</p>
<p>env：JNI接口指针</p>
<p><strong>五、全局引用和局部引用</strong></p>
<p><strong>(一)、创建全局引用</strong></p>
<p>jobject NewGlobalRef(JNIEnv *env,object obj);</p>
<p>给对象obj创建一个全局引用，obj可以是全局或局部引用。全局引用必须通过DeleteGlobalRef()显示处理。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>obj：object对象</p>
<p>返回：</p>
<p>全局引用jobject，如果内存溢出则返回NULL</p>
<p><strong>(二)、删除全局引用</strong></p>
<p>void DeleteGlobalRef(JNIEnv *env,jobject globalRef);</p>
<p>删除全局引用</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>globalRef：需要被删除的全局引用</p>
<p><strong>(三)、删除局部引用</strong></p>
<p>局部引用只在本地接口调用时的生命周期内有效，当本地方法返回时，它们会被自动释放。每个局部引用都会消耗一定的虚拟机资源，虽然局部引用可以被自动销毁，但是程序员也需要注意不要在本地方法中过度分配局部引用，过度分配局部引用会导致虚拟机在执行本地方法时内存溢出。</p>
<p>void DeleteLocalRef(JNIEnv *env, jobject localRef);</p>
<p>通过localRef删除局部引用</p>
<p>参数解释</p>
<p>env：JNI接口指针</p>
<p>localRef：需要被删除的局部引用</p>
<p>JDK/JRE 1.1提供了上面的DeleteLocalRef函数，这样程序员就可以手动删除本地引用。</p>
<p>从JDK/JRE 1.2开始，提供可一组生命周期管理的函数，他们是下面四个函数。</p>
<p><strong>(四)、设定局部变量的容量</strong></p>
<p>jint EnsureLocalCapacity(JNIEnv *env,jint capacity);</p>
<p>在当前线程中，通过传入一个容量capacity，，限制局部引用创建的数量。成功则返回0，否则返回一个负数，并抛出一个OutOfMemoryError。VM会自动确保至少可以创建16个局部引用。</p>
<p>参数解释</p>
<p>env：JNI接口指针</p>
<p>capacity：容量</p>
<p>返回：</p>
<p>成功返回0，失败返回一个负数，并会抛出一个OutOfMemoryError</p>
<p>为了向后兼容，如果虚拟机创建了超出容量的局部引用。VM调用FatalError，来保证不能创建更多的本地引用。(如果是debug模式，虚拟机回想用户发出warning，并提示创建了更多的局部引用，在JDK中，程序员可以提供-verbose：jni命令行选项来打开这个消息)</p>
<p><strong>(五)、释放一个局部引用</strong></p>
<p>jobject PopLocalFrame(JNIEnv *env,jobject result)</p>
<p>弹出当前的局部引用帧，并且释放所有的局部引用。返回在之前局部引用帧与给定result对象对应的局部引用。如果不需要返回任何引用，则设置result为NULL</p>
<p>参数解释</p>
<p>env：JNI接口指针</p>
<p>result：需要释放的局部引用</p>
<p><strong>(六)、创建一个局部引用</strong></p>
<p>jobject NewLocalRef(JNIEnv *env,jobject ref);</p>
<p>创建一个引用自ref的局部引用。ref可以是全局或者局部引用，如果ref为NULL，则返回NULL。</p>
<p>参数解释</p>
<p>env：JNI接口指针</p>
<p>ref：可以试试局部引用也可以是全局引用。</p>
<p><strong>(七)、弱全局引用</strong></p>
<p>弱全局引用是一种特殊的全局引用，不像一般的全局引用，一个弱全局引用允许底层Java对象能够被垃圾回收。弱全局引用能够应用在任何全局或局部引用被使用的地方。当垃圾回收器运行的时候，如果对象只被弱引用所引用时，它将释放底层变量。一个弱阮菊引用指向一个被释放的对象相当于等于NULL。编程人员可以通过使用isSampleObject对比弱引用和NULL来检测一个弱全局应用是否指向一个被释放的对象。弱全局引用在JNI中是Java弱引用的一个简化版本，在Java平台API中有有效。</p>
<p>当Native方法正在运行的时候，垃圾回收器可能正在工作，被弱引用所指向的对象可能在任何时候被释放。弱全局引用能够应用在任何全局引用所使用的地方，通常是不太适合那么做的，因为它们可能在不注意的时候编程NULL。</p>
<p>当IsSampleObject能够识别一个弱全局引用是不是指向一个被释放的对象，但是这不妨碍这个对象在被检测之后马上被释放。这就说明了，程序员不能依赖这个方法来识别一个弱全局引用是否能够在后续的JNI函数调用中被使用。</p>
<p>如果想解决上述的问题，建议使用JNI函数NewLocalRef或者NewGlobalRef来用标准的全局也引用或者局部引用来指向相同的对象。如果这个独享已经被释放了这些函数会返回NULL。否则会返回一个强引用(这样就可以保证这个对象不会被释放)。当不需要访问这个对象时，新的引用必须显式被删除。</p>
<p><strong>1、创建全局弱引用</strong></p>
<p>jweak NewWeakGlobalRef(JNIEnv *env,jobject obj);</p>
<p>创建一个新的弱全局引用。如果obj指向NULL，则返回NULL。如果VM内存溢出，将会抛出异常OutOfMemoryError。</p>
<p>参数解释</p>
<p>env：JNI接口指针</p>
<p>obj：引用对象</p>
<p>返回：</p>
<p>全局弱引用</p>
<p><strong>2、删除全局弱引用</strong></p>
<p>void DeleteWeakGlobalRef(JNIEnv *env,jweak obj);</p>
<p>VM根据所给定的弱全局引用删除对应的资源。</p>
<p>参数解释</p>
<p>env：JNI接口指针</p>
<p>obj：将删除的弱全局引用</p>
<p><strong>六、对象操作</strong></p>
<p><strong>(一)、直接创建一个Java对象</strong></p>
<p>jobject AllocObject(JNIEnv *env,jclass clazz);</p>
<p>不借助任何构造函数的情况下分配一个新的Java对象，返回对象的一个引用。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz:：Java类对象</p>
<p>返回：</p>
<p>返回一个Java对象，如果该对象无法被创建，则返回NULL。</p>
<p>异常：</p>
<p>如果该类是接口或者是抽象类，则抛出InstantiationException</p>
<p>如果是内存溢出，则抛出OutOfMemoryError</p>
<p><strong>(二)、根据某个构造函数来创建Java对象</strong></p>
<p>jobject NewObject(JNIEnv *env,jclass clazz,jmethodID methodID,...);</p>
<p>jobject NewObjectA(JNIEnv *env,jclass clazz,jmethodID methodID,const jvalue *args);</p>
<p>jobject NewObjectV(JNIEnv *env,jclass clazz,jmethodID methodID,va_list args);</p>
<p>构造一个新的Java对象，methodID表明需要调用一个构造函数。这个ID必须通过调用GetMethodID()获得，GetMethodID()为函数名，void(V)为返回值。clazz参数不能纸箱一个数组类</p>
<p>NewObject：需要把所有构造函数的入参，放在参数methodID之后。NewObject()接受这些参数并将它们传递给需要被调用的Java的构造函数</p>
<p>NewObjectA：在methodID后面，放了一个类型为jvalue的参数数组——args，该数组存放着所有需要传递给构造函数的参数。NewObjectA()接收到这个数组中的所有参数，并且按照顺序将它们传递给需要调用的Java方法。</p>
<p>NewObjectV：在methodID后面，放了一个类型为va_list的args，参数存放着所有需要传递给构造函数的参数。NewObjectv()接收到所有的参数，并且按照顺序将它们传递给需要调用的Java方法。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz:：Java类</p>
<p>methodID：构造函数的方法ID</p>
<p>附加参数：</p>
<p>NewObject的附加参数：arguments是构造函数的参数</p>
<p>NewObjectA的附加参数：args是构造函数的参数数组</p>
<p>NewObjectV的附加参数：args是构造函数的参数list</p>
<p>返回：</p>
<p>Java对象，如果无法创建该对象，则返回NULL</p>
<p>异常：</p>
<p>如果传入的类是接口或者抽象类，则抛出InstantiationException</p>
<p>如果内存溢出，则抛出OutOfMemoryError</p>
<p>所有的异常都是通过构造函数抛出</p>
<p><strong>(三)、获取某个对象的“类”</strong></p>
<p>jclass GetObjectClass(JNIEnv *env,object obj);</p>
<p>返回obj对应的类</p>
<p>参数解释</p>
<p>env：JNI接口指针</p>
<p>obj：Java对象，不能为NULL</p>
<p>参数：</p>
<p>env：JNI接口指针</p>
<p>obj：JAVA对象，不能为NULL</p>
<p>返回：</p>
<p>返回一个Java“类”对象</p>
<p><strong>(四)、获取某个对象的“类型”</strong></p>
<p>jobjectRefType GetObjectRefType(JNIEnv *env,jobject obj);</p>
<p>返回obj参数所以指向对象的类型，参数obj可以是局部变量，全局变量或者若全局引用。</p>
<p>参数解释</p>
<p>env：JNI接口指针</p>
<p>obj：局部、全局或弱全局引用</p>
<p>返回：</p>
<p>JNIInvalidRefType=0：代表obj参数不是有效的引用类型</p>
<p>JNILocalRefType=1：代表obj参数是局部变量类型</p>
<p>JNIGlobalRefType=2：代表obj参数是全局变量类型</p>
<p>JNIWeakGlobalRefType=3：代表obj参数是弱全局有效引用</p>
<p>无效的引用就是没有引用的引用。也就是说，obj的指针没有指向内存中创建函数时候的地址，或者已经从JNI函数中返回了。所以说NULL就是无效的引用。并且GetObjectRefType(env,NULL)将返回类型是JNIInvalidRefType。但是空引用返回的不是JNIInvalidRefType，而是它被创建时候的引用类型。</p>
<p>PS:不能在引用在删除的时候，调用该函数</p>
<p><strong>(五)、判断某个对象是否是某个“类”的子类</strong></p>
<p>jboolean IsInstanceOf(JNIEnv *env, jobject obj,jclass clazz);</p>
<p>测试obj是否是clazz的一个实例</p>
<p>参数：</p>
<p>env：JNI接口指针</p>
<p>obj：一个Java对象</p>
<p>clazz：一个Java的类</p>
<p>返回：</p>
<p>如果obj是clazz的实例，则返回JNI_TRUE；否则则返回JNI_FALSE；一个空对象可以是任何类的实例。</p>
<p><strong>(六)、判断两个引用是否指向同一个引用</strong></p>
<p>jboolean IsSampleObject(JNIEnv *env,jobject ref1,jobject ref2);</p>
<p>判断两个引用是否指向同一个对象</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>ref1：Java对象</p>
<p>ref2：Java对象</p>
<p>返回：</p>
<p>如果同一个类对象，返回JNI_TRUE；否则，返回JNI_FALSE；</p>
<p><strong>(七)、返回属性id</strong></p>
<p>jfieldID GetFieldID(JNIEnv *env,jclass clazz,const char *name,const char *sig);</p>
<p>获取某个类的非静态属性id。通过方法属性名以及·属性的签名(也就是属性的类型)，来确定对应的是哪个属性。通过检索这个属性ID，我们就可以调用Get Field和Set Field了，就是我们常用的get和set`方法</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：一个Java类对象</p>
<p>name：以"0"结尾的，而且字符类型是"utf-8"的属性名称</p>
<p>sig：以"0"结尾的，而且字符类型是"utf-8"的属性签名</p>
<p>返回</p>
<p>属性对应ID，如果操作失败，则返回NULL</p>
<p>异常：</p>
<p>如果找不到指定的属性，则抛出NoSuchFieldError</p>
<p>如果类初始化失败，则抛出ExceptionInitializerError</p>
<p>如果内存不足了，则抛出OutOfMemoryError</p>
<p>PS：GetFieldID()可能会导致还未初始化的类开始初始化，同时在获取数组的长度不能使用GetFieldID()，而应该使用GetArrayLength()。</p>
<p><strong>(八)、返回属性id系列</strong></p>
<p>NativeType GetField(JNIEnv *env,jobject obj,jfieldID fielD);</p>
<p>返回某个类的非静态属性的值，这是一组函数的简称，具体如下：</p>
<p>jobject GetObjectField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>jboolean GetBooleanField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>jbyte GetByteField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>jchar GetCharField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>jshort GetShortField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>jint GetIntField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>jlong GetLongField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>jfloat GetFloatField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>jdouble GetDoubleField(JNIEnv *env,jobject obj,jfieldID fielD)</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>obj：Java对象，不能为空</p>
<p>fieldID：有效的fieldID</p>
<p>返回：</p>
<p>对应属性的值</p>
<p><strong>(九)、设置属性id系列</strong></p>
<p>void SetField(JNIEnv *env,jobject obj,jfieldID fieldID,NativeType value)</p>
<p>设置某个类的的非静态属性的值。其中具体哪个属性通过GetFieldID()来确定哪个属性。这是一组函数的简称，具体如下：</p>
<p>void SetObjectField(jobject)</p>
<p>void SetBooleanField(jboolean)</p>
<p>void SetByteField(jbyte)</p>
<p>void SetCharField(jchar)</p>
<p>void SetShortField(jshort)</p>
<p>void SetIntField(jint)</p>
<p>void SetLongField(jlong)</p>
<p>void SetFloatField(jfloat)</p>
<p>void SetDoubleField(jdouble)</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>obj：Java对象，不能为空</p>
<p>fieldID：有效的属性ID</p>
<p>value：属性的新值</p>
<p><strong>(十)、获取某个类的某个方法id</strong></p>
<p>jmethodID GetMethodID(JNIEnv *env,jclass clazz,const char*name,const char* sig);</p>
<p>返回某个类或者接口的方法ID，该方法可以是被定义在clazz的父类中，然后被clazz继承。我们是根据方法的名字以及签名来确定一个方法的。</p>
<p>PS:GetMethodID()会造成还未初始化的类，进行初始化</p>
<p>如果想获取构造函数的ID,请提供init作为方法名称，并将void(V)作为返回类型</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：Java类对象</p>
<p>name：以0结尾的，并且是"utf-8"的字符串的方法名称</p>
<p>sig：以0结尾的，并且是"utf-8"的字符串的方法签名</p>
<p>返回：</p>
<p>返回一个方法ID，没有找到指定的方法，则返回NULL</p>
<p>异常：</p>
<p>如果找不到指定的方法，则抛出NoSuchMethodError</p>
<p>如果累初始化失败，则抛出ExceptionInInitializerError</p>
<p>如果内存不够，则抛出OutOfMemoryError</p>
<p><strong>(十一)、调用Java实例的某个非静态方法“系列”</strong></p>
<p>NativeType CallMethod(JNIEnv *env,jobject obj,jmethodID methodID,...);</p>
<p>NativeType CallMethodA(JNIEnv *env,jobjct obj,jmethodID methodID ,const jvalue *args);</p>
<p>NativeType CallMethodV(JNEnv *env,jobject obj,jmethodID methodID,va_list args);</p>
<p>这一些列都是在native中调用Java对象的某个非静态方法，它们的不同点在于传参不同。是根据方法ID来指定对应的Java对象的某个方法。methodID参数需要调用GetMethodID()获取。</p>
<p>PS：当需要调用某个"private"函数或者构造函数时，这个methodID必须是obj类的方法，不能是它的父类的方法。</p>
<p>下面我们来看下他们的不同点</p>
<p>CallMethod：需要把方法的入参放在参数methodID后面。CallMethod()其实把这些参数传递给需要调用的Java方法。</p>
<p>CallMethodA：在methodID后面，有一个类型为jvalue的args数组，该数组存放所有需要传递给构造函数的参数。CallMethodA()收到这个数组中的参数，是按照顺序将他们传递给对应的Java方法</p>
<p>CallMethodV：在methodID后面，有一个类型Wieva_list的参数args，它存放着所有需要传递给构造函数的参数。CallMethodV()接收所有的参数，并且按照顺序将它们传递给需要调用的Java方法。</p>
<p>CallMethod Routine Name Native Type</p>
<p>CallVoidMethod()</p>
<p>CallVoidMethodA() void</p>
<p>CallVoidMethodV()</p>
<p>CallObjectMethod()</p>
<p>CallObjectMethodA() jobject</p>
<p>CallObjectMethodV()</p>
<p>CallBooleanMethod()</p>
<p>CallBooleanMethodA() jboolean</p>
<p>CallBooleanMethodV()</p>
<p>CallByteMethod()</p>
<p>CallByteMethodA() jbyte</p>
<p>CallByteMethodV()</p>
<p>CallCharMethod()</p>
<p>CallCharMethodA() jchar</p>
<p>CallCharMethodV()</p>
<p>CallShortMethod()</p>
<p>CallShortMethodA() jshort</p>
<p>CallShortMethodV()</p>
<p>CallIntMethod()</p>
<p>CallIntMethodA() jint</p>
<p>CallIntMethodV()</p>
<p>CallLongMethod()</p>
<p>CallLongMethodA()</p>
<p>CallLongMethodV()</p>
<p>CallFloatMethod()</p>
<p>CallFloatMethodA() jlong</p>
<p>CallFloatMethodV()</p>
<p>CallDoubleMethod()</p>
<p>CallDoubleMethodA() jfloat</p>
<p>CallDoubleMethodV()</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>obj：对应的Java对象</p>
<p>methodID：某个方法的方法id</p>
<p>返回：</p>
<p>返回调用Java方法对应的结果</p>
<p>异常：</p>
<p>在Java方法执行过程中产生的异常。</p>
<p><strong>(十二)、调用某个类的非抽象方法</strong></p>
<p>调用父类中的实例方法，如下系列</p>
<p>CallNonvirtualMethod</p>
<p>CallNonvirtualMethodA</p>
<p>CallNonvirtualMethodV</p>
<p>具体如下：</p>
<p>NativeType CallNonvirtualMethod(JNIEnv *env,jobject obj,jclass clazz,jmethodID methodID,....);</p>
<p>NativeType CallNonvirtualMethodA(JNIEnv *env,jobject obj,jclass clazz,jmethodID methodID,const jvalue *args);</p>
<p>NativeType CallNonvirtualMethodV(JNIEnv *env, jobject obj,</p>
<p>jclass clazz, jmethodID methodID, va_list args);</p>
<p>这一系列操作就是根据特定的类，和其方法ID来调用Java对象的实例的非静态方法，methodID参数需要调用GetMethodID()获取。</p>
<p>CallNonvirtualMethod和CallMethod是不同的，其中CallNonvirtualMethod是基于"类"，而和CallMethod是基于类的对象。所以说CallNonvirtualMethod`的入参是 clazz，methodID必须来源与obi的类，而不是它的父类</p>
<p>下面我们来看下他们的不同点</p>
<p>CallNonvirtualMethod ：需要把方法的入参放在参数methodID后面。CallNonvirtualMethod()其实把这些参数传递给需要调用的Java方法。</p>
<p>CallNonvirtualMethod：在methodID后面，有一个类型为jvalue的args数组，该数组存放所有需要传递给构造函数的参数。CallNonvirtualMethod()收到这个数组中的参数，是按照顺序将他们传递给对应的Java方法</p>
<p>CallNonvirtualMethodV ：在methodID后面，有一个类型Wieva_list的参数args，它存放着所有需要传递给构造函数的参数。 CallNonvirtualMethodV()接收所有的参数，并且按照顺序将它们传递给需要调用的Java方法。</p>
<p>将上面这系列方法展开如下：</p>
<p>CallNonvirtualMethod Routine Name Native Type</p>
<p>CallNonvirtualVoidMethod()</p>
<p>CallNonvirtualVoidMethodA() void</p>
<p>CallNonvirtualVoidMethodV()</p>
<p>CallNonvirtualObjectMethod()</p>
<p>CallNonvirtualObjectMethodA() jobject</p>
<p>CallNonvirtualObjectMethodV()</p>
<p>CallNonvirtualBooleanMethod()</p>
<p>CallNonvirtualBooleanMethodA() jboolean</p>
<p>CallNonvirtualBooleanMethodV()</p>
<p>CallNonvirtualByteMethod()</p>
<p>CallNonvirtualByteMethodA() jbyte</p>
<p>CallNonvirtualByteMethodV()</p>
<p>CallNonvirtualCharMethod()</p>
<p>CallNonvirtualCharMethodA() jchar</p>
<p>CallNonvirtualCharMethodV()</p>
<p>CallNonvirtualShortMethod()</p>
<p>CallNonvirtualShortMethodA() jshort</p>
<p>CallNonvirtualShortMethodV()</p>
<p>CallNonvirtualIntMethod()</p>
<p>CallNonvirtualIntMethodA() jint</p>
<p>CallNonvirtualIntMethodV()</p>
<p>CallNonvirtualLongMethod()</p>
<p>CallNonvirtualLongMethodA() jlong</p>
<p>CallNonvirtualLongMethodV()</p>
<p>CallNonvirtualFloatMethod()</p>
<p>CallNonvirtualFloatMethodA() jfloat</p>
<p>CallNonvirtualFloatMethodV()</p>
<p>CallNonvirtualDoubleMethod()</p>
<p>CallNonvirtualDoubleMethodA() jdouble</p>
<p>CallNonvirtualDoubleMethodV()</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>obj：Java对象</p>
<p>clazz：Java类</p>
<p>methodID：方法ID</p>
<p>返回：</p>
<p>调用Java方法的结果</p>
<p>抛出异常：</p>
<p>在Java方法中执行过程可能产生的异常</p>
<p><strong>(十三)、获取静态属性</strong></p>
<p>jfieldID GetStaticFieldID(JNIEnv *env,jclass clazz,const char* name,const char *sig);</p>
<p>获取某个类的某个静态属性ID，根据属性名以及标签来确定是哪个属性。GetStaticField()和SetStaticField()通过使用属性ID来对属性进行操作的。如果这个类还没有初始化，直接调用GetStaticFieldID()会引起这个类进行初始化。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：Java类</p>
<p>name：静态属性的属性名，是一个编码格式"utf-8"并且以0结尾的字符串。</p>
<p>sig：属性的签名，是一个编码格式"utf-8"并且以0结尾的字符串。</p>
<p>返回：</p>
<p>返回静态属性ID，如果指定的静态属性无法找则返回NULL</p>
<p>异常：</p>
<p>如果指定的静态属性无法找到则抛出NoSuchFieldError</p>
<p>如果类在初始化失败，则抛出ExceptionInInitializerError</p>
<p>如果内存不够，则抛出OutOfMemoryError</p>
<p><strong>(十四)、获取静态属性系列</strong></p>
<p>NativeType GetStaticField(JNIEnv *env,jclass clazz,jfieldID fieldID);</p>
<p>这个系列返回一个对象的静态属性的值。可以通过GetStaticFieldID()来获取静态属性的的ID，有了这个ID，我们就可以获取这个对其进行操作了</p>
<p>下面表明了函数名和函数的返回值，所以只需要替换GetStaticField中的类替换为该字段的Java类型或者表中的实际静态字段存取器。并将NativeType替换为相应的本地类型</p>
<p>GetStaticField Routine Name Native Type</p>
<p>GetStaticObjectField() jobject</p>
<p>GetStaticBooleanField() jboolean</p>
<p>GetStaticByteField() jbyte</p>
<p>GetStaticCharField() jchar</p>
<p>GetStaticShortField() jshort</p>
<p>GetStaticIntField() jint</p>
<p>GetStaticLongField() jlong</p>
<p>GetStaticFloatField() jfloat</p>
<p>GetStaticDoubleField() jdouble</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：Java类</p>
<p>field：静态属性ID</p>
<p>返回：</p>
<p>返回静态属性</p>
<p><strong>(十五)、设置静态属性系列</strong></p>
<p>void SetStaticField(JNIEnv *env,jclass clazz,jfieldID fieldID,NativeType value);</p>
<p>这个系列是设置类的静态属性的值。可以通过GetStaticFieldID()来获取静态属性的ID。</p>
<p>下面详细介绍了函数名和其值，你可以通过SetStatic并传入的NativeType来设置Java中的静态属性。</p>
<p>SetStaticField Routine Name NativeType</p>
<p>SetStaticObjectField() jobject</p>
<p>SetStaticBooleanField() jboolean</p>
<p>SetStaticByteField() jbyte</p>
<p>SetStaticCharField() jchar</p>
<p>SetStaticShortField() jshort</p>
<p>SetStaticIntField() jint</p>
<p>SetStaticLongField() jlong</p>
<p>SetStaticFloatField() jfloat</p>
<p>SetStaticDoubleField() jdouble</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：Java类</p>
<p>field：静态属性ID</p>
<p>value：设置的值</p>
<p><strong>(十六)、获取静态函数ID</strong></p>
<p>jmethodID GetStaticMethodID(JNIEnv *env,jclass clazz,const char *name,const char sig);</p>
<p>返回类的静态方法ID，通过它的方法名以及签名来确定哪个方法。如果这个类还没被初始化，调用GetStaticMethodID()将会导致这个类初始化。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：Java类</p>
<p>name：静态方法的方法名，以"utf-8"编码的，并且以0结尾的字符串</p>
<p>sig：方法签名，以"utf-8"编码的，并且以0结尾的字符串</p>
<p>返回：</p>
<p>返回方法ID，如果操作失败，则返回NULL</p>
<p>异常：</p>
<p>如果没有找到对应的静态方法，则抛出NoSuchMethodError</p>
<p>如果类初始化失败，则抛出ExceptionInInitializerError</p>
<p>如果系统内存不足，则抛出OutOfMemoryError</p>
<p><strong>(十七)、调用静态函数系列</strong></p>
<p>NativeType CallStaticMethod(JNIEnv *env,jclass clazz,jmethodID methodID,...);</p>
<p>NativeType CallStaticMethodA(JNIEnv *env,jclass clazz,jmethodID methodID,... jvalue *args);</p>
<p>NativeType CallStaticMethodV(JNIEnv *env,jclass,jmethodID methodid, va_list args)</p>
<p>根据指定的方法ID，就可以操作Java对象的静态方法了。可以通过GetStaticMethodID()来获得methodID。方法的ID必须是clazz的，而不是其父类的方法ID。</p>
<p>下面就是详细的方法了</p>
<p>CallStaticMethod Routine Name Native Type</p>
<p>CallStaticVoidMethod()</p>
<p>CallStaticVoidMethodA() void</p>
<p>CallStaticVoidMethodV()</p>
<p>CallStaticObjectMethod()</p>
<p>CallStaticObjectMethodA() jobject</p>
<p>CallStaticObjectMethodV()</p>
<p>CallStaticBooleanMethod()</p>
<p>CallStaticBooleanMethodA() jboolean</p>
<p>CallStaticBooleanMethodV()</p>
<p>CallStaticByteMethod()</p>
<p>CallStaticByteMethodA() jbyte</p>
<p>CallStaticByteMethodV()</p>
<p>CallStaticCharMethod()</p>
<p>CallStaticCharMethodA() jchar</p>
<p>CallStaticCharMethodV()</p>
<p>CallStaticShortMethod()</p>
<p>CallStaticShortMethodA() jshort</p>
<p>CallStaticShortMethodV()</p>
<p>CallStaticIntMethod()</p>
<p>CallStaticIntMethodA() jint</p>
<p>CallStaticIntMethodV()</p>
<p>CallStaticLongMethod()</p>
<p>CallStaticLongMethodA() jlong</p>
<p>CallStaticLongMethodV()</p>
<p>CallStaticFloatMethod()</p>
<p>CallStaticFloatMethodA() jfloat</p>
<p>CallStaticFloatMethodV()</p>
<p>CallStaticDoubleMethod()</p>
<p>CallStaticDoubleMethodA() jdouble</p>
<p>CallStaticDoubleMethodV()</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：Java类</p>
<p>methodID：静态方法ID</p>
<p>返回：</p>
<p>返回静态的Java方法的调用方法</p>
<p>异常：</p>
<p>在Java方法中执行中抛出的异常</p>
<p><strong>七、字符串操作</strong></p>
<p><strong>（一)、创建一个字符串</strong></p>
<p>jstring NewString(JNIEnv *env,const jchar *unicodeChars,jszie len);</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>unicodeChars：指向Unicode字符串的指针</p>
<p>len：unicode字符串的长度</p>
<p>返回：</p>
<p>返回一个Java字符串对象，如果该字符串无法被创建在，则返回NULL</p>
<p>异常：</p>
<p>如果内存不足，则抛出OutOfMemoryError</p>
<p><strong>（二)、获取字符串的长度</strong></p>
<p>jsize GetStringLength(JNIEnv *env,jstring string);</p>
<p>返回Java字符串的长度(unicode字符的个数)</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>string：Java字符串对象</p>
<p>返回：</p>
<p>返回Java字符串的长度</p>
<p><strong>（三)、获取字符串的指针</strong></p>
<p>const jchar* GetStringChar(JNIEnv *env,jstring string , jboolean *isCopy);</p>
<p>返回指向字符串的UNICODE字符数组的指针，该指针一直有效直到被ReleaseStringchars()函数调用。</p>
<p>如果isCopy为非空，则在复制完成后将isCopy设为JNI_TRUE。如果没有复制，则设为JNI_FALSE。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>string：Java字符串对象</p>
<p>isCopy：指向布尔值的指针</p>
<p>返回：</p>
<p>返回一个指向unicode字符串的指针，如果操作失败，则返回NULL</p>
<p><strong>（四)、释放字符串</strong></p>
<p>void ReleaseStringChars(JNIEnv *env,jstring string,const jchar *chars);</p>
<p>通过VM，native代码不会再访问chars了。参数chars是一个指针。可以通过GetStringChars()函数获得。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>string：Java字符串对象</p>
<p>chars：指向Unicode字符串的指针</p>
<p><strong>（五)、创建一个UTF-8的字符串</strong></p>
<p>jstring NewStringUTF(JNIEnv *env,const char *bytes);</p>
<p>创建一个UTF-8的字符串。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>bytes：指向UTF-8字符串的指针</p>
<p>返回：</p>
<p>Java字符串对象，如果无法构造该字符串，则为NULL。</p>
<p>异常：</p>
<p>如果系统内存不足，则抛出OutOfMemoryError</p>
<p><strong>（六)、获取一个UTF-8的字符串的长度</strong></p>
<p>jsize GetStringUTFLength(JNIEnv *env,jstring string);</p>
<p>以字节为单位，返回字符串UTF-8的长度。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>String：Java字符串对象</p>
<p>返回：</p>
<p>字符串的UTF-8的长度</p>
<p><strong>（七)、获取StringUTFChars的指针</strong></p>
<p>const char *GetStringUFTChars(JNIEnv *env, jString string, jboolean *isCopy);</p>
<p>返回指向UTF-8字符数组的指针，除非该数组被ReleaseStringUTFChars()函数调用释放，否则一直有效。</p>
<p>如果isCopy不是NULL，*isCopy在赋值完成后即被设置为JNI_TRUE。如果未复制，则设置为JNI_FALSE。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>String：Java字符串对象</p>
<p>isCopy：指向布尔值的指针</p>
<p>返回：</p>
<p>指向UTF-8的字符串指针，如果操作是啊白，则返回NULL</p>
<p><strong>（八)、释放UTFChars</strong></p>
<p>void ReleaseStringUTFChars(JNIEnv *env,jstring string,const char *urf)</p>
<p>通过虚拟机，native代码不再访问了utf了。utf是一个指针，可以调用GetStringUTFChars()获取。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>string：Java字符串对象</p>
<p>utf：指向utf-8字符串的指针</p>
<p>注意：在JDK/JRE 1.1，程序员可以在用户提供的缓冲区获取基本类型数组元素，从JDK/JRE1.2开始，提供了额外方法，这些方法允许在用户提供的缓冲区获取Unicode字符(UTF-16编码)或者是UTF-8的字符。这些方法如下：</p>
<p><strong>（九)、字符串操作方法</strong></p>
<p><strong>1、截取一个字符串</strong></p>
<p>void GetStringRegion(JNIEnv *env,jstring str,jsize start,jsize len,jchar *buf)</p>
<p>在str(Unicode字符)从start位置开始截取len长度放置在buf中。如果越界，则抛出StringIndexOutOfBoundsException。</p>
<p><strong>2、 截取一个字符串并将其转换为UTF-8格式</strong></p>
<p>void GetStringUTFRegion(JNIEnv *env,jstring str,jsize start ,jsize len,char *buf);</p>
<p>将str(Unicode字符串)从start位置开始截取len长度并且将其转换为UTF-8编码，然后将结果防止在buf中。</p>
<p><strong>3 、截取一个字符串并将其转换为UTF-8格式</strong></p>
<p>const jchar * GetStringCritical(JNIEnv *env,jstring string,jboolean *isCopy);</p>
<p>void ReleaseStringCritical(JNIEnv *env,jstring string,cost jchar * carray);</p>
<p>上面这两个函数有点类似于GetStringChars()和ReleaseStringChars()功能。如果可能的话虚拟机会返回一个指向字符串元素的指针；否则，则返回一个复制的副本。</p>
<p>PS：GetStringChars()和ReleaseStringChars()这里两个函数有很大的限制。在使用这两个函数时，这两个函数中间的代码不能调用任何让线程阻塞或者等待JVM的其他线程的本地函数或者JNI函数。有了这些限制，JVM就可以在本地方法持有一个从GetStringCritical得到的字符串的指指针时，禁止GC。当GC被禁止时，任何线程如果出发GC的话，都会被阻塞。而GetStringChars()和ReleaseStringChars()这两个函数中间的任何本地代码都不可以执行会导致阻塞的调用或者为新对象在JVM中分配内存。否则，JVM有可能死活，想象一下这样的场景：</p>
<p>1、只有当前线程触发的GC完成阻塞并释放GC时，由其他线程出发的GC才可能由阻塞中释放出来继续执行。</p>
<p>2、在这个过程中，当前线程会一直阻塞，因为任何阻塞性调用都需要获取一个正在被其他线程持有的锁，而其他线程正等待GC。</p>
<p>GetStringChars()和ReleaseStringChars()的交替迭代调用是安全的，这种情况下，它们的使用必须有严格的顺序限制。而且，我们一定要记住检查是否因为内存溢出而导致它的返回值是NULL。因为JVM在执行GetStringChars()这个函数时，仍有发生数据复制的可能性，尤其是当JVM在内存存储的数组不连续时，为了返回一个指向连续内存空间的指针，JVM必须复制所有数据。</p>
<p>总之，为了避免死锁，在GetStringChars()和ReleaseStringChars()`之间不要调用任何JNI函数。</p>
<p><strong>八、数组操作</strong></p>
<p><strong>(一)、获取数组的长度</strong></p>
<p>jsize GetArrayLength(JNIEnv *env,jarray array)</p>
<p>返回数组的长度</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>array：Java数组</p>
<p>返回：</p>
<p>数组的长度</p>
<p><strong>(二)、创建对象数组</strong></p>
<p>jobjectArray NewObjectArray(JNIEnv *env,jsize length,jclass elementClass, jobject initialElement);</p>
<p>创建一个新的对象数组，它的元素的类型是elementClass，并且所有元素的默认值是initialElement。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>length：数组大小</p>
<p>elementClass：数组元素类</p>
<p>initialElement：数组元素的初始值</p>
<p>返回：</p>
<p>Java数组对象，如果无法构造数组，则返回NULL</p>
<p>异常：</p>
<p>如果内存不足，则抛出OutOfMemoryError</p>
<p><strong>(三)、获取数组元中的某个元素</strong></p>
<p>jobject GetObjectArrayElement(JNIEnv *env,jobjectArray array,jsize index);</p>
<p>返回元素中某个位置的元素</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>array：Java数组</p>
<p>index：数组下标</p>
<p>返回：</p>
<p>Java对象</p>
<p>异常：</p>
<p>如果index下标不是一个有效的下标，则会抛出ArrayIndexOutOfBoundsException</p>
<p><strong>(四)、设置数组中某个元素的值</strong></p>
<p>void SetObjectArrayElement(JNIEnv *env,jobjectArray array,jsize index,jobject value);</p>
<p>设置下标为index元素的值。</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>array：Java数组</p>
<p>index：数组下标</p>
<p>value：数组元素的新值</p>
<p>异常：</p>
<p>如果index不是有效下标，则会抛出ArrayIndexOutOfBoundsException</p>
<p>如果value不是元素类的子类，则会抛出ArrayStoreException</p>
<p><strong>(五)、创建基本类型数组系列</strong></p>
<p>ArrayType NewArray(JNIEnv *env,jsize length);</p>
<p>用于构造基本类型数组对象的一系列操作。下面说明了特定基本类型数组的创建函数。可以把NewArray替换为某个实际的基本类型数组创建函数 ，然后将ArrayType替换为相应的数组类型</p>
<p>NewArray Routines Array Type</p>
<p>NewBooleanArray() jbooleanArray</p>
<p>NewByteArray() jbyteArray</p>
<p>NewCharArray() jcharArray</p>
<p>NewShortArray() jshortArray</p>
<p>NewIntArray() jintArray</p>
<p>NewLongArray() jlongArray</p>
<p>NewFloatArray() jfloatArray</p>
<p>NewDoubleArray() jdoubleArray</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>length：数组长度</p>
<p>返回：</p>
<p>Java数组，如果无法创建该数组，则返回NULL。</p>
<p><strong>(六)、获取基本类型数组的中数组指针系列</strong></p>
<p>NativeType * GetArrayElements(JNIEnv *env,ArrayType array,jboolean * isCopy);</p>
<p>一组返回类型是基本类型的数组指针。在调用相应的ReleaseArrayElements()函数前将一直有效。由于返回的数组可能是Java数组的副本，因此，对返回数组的变更没有在基本类型中反应出来。除非了调用</p>
<p>一组返回基本类型数组体的函数。结果在调用相应的 ReleaseArrayElements()函数前将一直有效。由于返回的数组可能是 Java 数组的副本，因此对返回数组的更改不必在基本类型数组中反映出来，直到调用``ReleaseArrayElements()`函数。</p>
<p>如果isCopy不是NULL，*isCopy在复制完成后即被设为JNI_TRUE。如果未复制，则设为JNI_FALSE。</p>
<p>下面说明了特定的基本类型数组元素的具体函数：</p>
<p>将GetArrayElements替换为表中某个实际的基本> 类型的函数</p>
<p>将ArrayType替换为对应的数组类型</p>
<p>将NativeType替换为本地变量</p>
<p>不管布尔数组在Java虚拟机总如何表示，GetBooleanArrayElements()将始终返回一个jboolean类型的指针，其中每一个字节代表一个元素(开包表示)。内存中将确保所有其他类型的数组为连续的。</p>
<p>GetArrayElements Routines Array Type Native Type</p>
<p>GetBooleanArrayElements() jbooleanArray jboolean</p>
<p>GetByteArrayElements() jbyteArray jbyte</p>
<p>GetCharArrayElements() jcharArray jchar</p>
<p>GetShortArrayElements() jshortArray jshort</p>
<p>GetIntArrayElements() jintArray jint</p>
<p>GetLongArrayElements() jlongArray jlong</p>
<p>GetFloatArrayElements() jfloatArray jfloat</p>
<p>GetDoubleArrayElements() jdoubleArray jdouble</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>array：Java数组</p>
<p>isCopy：指向布尔值的指针</p>
<p>返回：</p>
<p>返回指向数组元素的指针，如果操作失败，则返回NULL</p>
<p><strong>(七)、复制过去基本类型的数组系列</strong></p>
<p>void Get ArrayRegion(JNIEnv *env,ArrayType array,jsize start,jsize len,NativeType *buf);</p>
<p>复制基本类型的数组给buff</p>
<p>下面说明了特定的基本类型数组元素的具体函数：</p>
<p>将Get ArrayRegion替换下面中某个实际的基本> 类型的函数</p>
<p>将ArrayType替换为对应的基本数组类型</p>
<p>将NativeType替换为本地变量</p>
<p>GetArrayRegion Routine Array Type Native Type</p>
<p>GetBooleanArrayRegion() jbooleanArray jboolean</p>
<p>GetByteArrayRegion() jbyteArray jbyte</p>
<p>GetCharArrayRegion() jcharArray jchar</p>
<p>GetShortArrayRegion() jshortArray jhort</p>
<p>GetIntArrayRegion() jintArray jint</p>
<p>GetLongArrayRegion() jlongArray jlong</p>
<p>GetFloatArrayRegion() jfloatArray jloat</p>
<p>GetDoubleArrayRegion() jdoubleArray jdouble</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>array：Java数组</p>
<p>start：开始索引</p>
<p>len：需要复制的长度</p>
<p>buf：目标buffer</p>
<p>异常：</p>
<p>如果索引无效，则抛出ArrayIndexOutOfBoundsException</p>
<p><strong>(八)、把基本类型数组的数组复制回来系列</strong></p>
<p>void Set ArrayRegion(JNIEnv *env,ArrayType array,jsize start,jsize len,const NativeType *buf);</p>
<p>主要是冲缓冲区复制基本类型的数组的函数</p>
<p>下面说明了特定的基本类型数组元素的具体函数：</p>
<p>将SetArrayRegion替换下面中某个实际的基本> 类型的函数</p>
<p>将ArrayType替换为对应的基本数组类型</p>
<p>将NativeType替换为本地变量</p>
<p>SetArrayRegion Routine Array Type Native Type</p>
<p>SetBooleanArrayRegion() jbooleanArray jboolean</p>
<p>SetByteArrayRegion() jbyteArray jbyte</p>
<p>SetCharArrayRegion() jcharArray jchar</p>
<p>SetShortArrayRegion() jshortArray jshort</p>
<p>SetIntArrayRegion() jintArray jint</p>
<p>SetLongArrayRegion() jlongArray jlong</p>
<p>SetFloatArrayRegion() jfloatArray jfloat</p>
<p>SetDoubleArrayRegion() jdoubleArray jdouble</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>array：Java数组</p>
<p>start：开始索引</p>
<p>len：需要复制的长度</p>
<p>buf：源buffer</p>
<p>异常：</p>
<p>如果索引无效则会抛出ArrayIndexOutOfBoundsException</p>
<p><strong>九、系统级别的操作</strong></p>
<p><strong>(一) 注册方法</strong></p>
<p>jint RegisterNatives(JNIEnv *env,jclass clazz,const JNINativeMethod *methods,jint nMethod);</p>
<p>根据clazz参数注册本地方法，methods参数制定JNINativeMethod结构数组，该数组包含本地方法的名字、签名及函数指针。其中名字及签名是指向编码为“UTF-8”的指针；nMethod参数表明数组中本地方法的个数。</p>
<p>这里说下JNINativeMethod这个结构体</p>
<p>typedef struct &#123;</p>
<p>char *name;</p>
<p>char *signature;</p>
<p>void *fnPtr;</p>
<p>&#125; JNINativeMethod;</p>
<p>参数解释：</p>
<p>env：JNI接口指针</p>
<p>clazz：Java类对象</p>
<p>methods：类中的native方法</p>
<p>nMethod：类中本地方法的个数</p>
<p>返回；</p>
<p>成功返回0，失败返回负数</p>
<p>异常：</p>
<p>如果没有找到指定的方法或者方法不是本地方法，则抛出NoSuchMethodError。</p>
<p><strong>(二) 注销方法</strong></p>
<p>jint UnregisterNatives(JNIEnv *env,jclass clazz);</p>
<p>注销本地方法。类回收之前还没有被函数注册的状态。该函数一般不能再Native代码中被调用，它为特定的程序提供了一种重加载重链接本地库的方法。</p>
<p>参数解释：</p>
<p>JNI：接口指针</p>
<p>clazz：Java类对象</p>
<p>返回：</p>
<p>注销成功返回0，失败返回负数</p>
<p><strong>总结：</strong></p>
<p><strong>常用的jni都总结到这里了，需要的可以收藏下；</strong></p>
<p><strong>下次会介绍java和jni之间的相互调用。</strong></p></div>  
</div>
            