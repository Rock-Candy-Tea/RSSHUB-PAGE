
---
title: 'Qt for Android（一） —— QT 中如何调用android方法｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2419'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 01:42:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=2419'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">背景：</h4>
<p>最近项目迁到 Android 平台下运行，因此涉及了不少 Qt for Android 的开发，遂记录下来并分享出来给大家。</p>
<p>QT 想要调用 android 的方法少不了 <code>QAndroidJniObject</code> 这个类，QT 官方文档对它有充分的解释说明:</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdoc.qt.io%2Fqt-5%2Fqandroidjniobject.html%23" target="_blank" rel="nofollow noopener noreferrer" title="https://doc.qt.io/qt-5/qandroidjniobject.html#" ref="nofollow noopener noreferrer">doc.qt.io/qt-5/qandro…</a></p>
<p>本篇文章是专栏系列的基础，只要学会 <code>QAndroidJniObject</code> 的使用，Qt for Android 就掌握大半了。<code>QAndroidJniObject</code> 属于 androidextras 模块，要使用它，需要在 pro 文件中加入下面的代码：</p>
<pre><code class="copyable">QT += androidextras
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是 CMake 项目，则需要加入下面的依赖：</p>
<pre><code class="copyable">AndroidExtras
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fforuok%2Farticle%2Fdetails%2F43459069" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/foruok/article/details/43459069" ref="nofollow noopener noreferrer">安晓辉 QtAndroid详解(1)：QAndroidJniObject</a></p>
</blockquote>
<p>androidextras 是从 Qt 5.2 引入的。这个模块内还包括了 <code>QAndroidJniEnvironment</code> 类，<code>QAndroidJniEnvironment</code>  代表 JNI 环境，也就是通常我们使用 JNI 编程时的 JNIEnv 。我们使用 Qt 进行 JNI 编程时，构造一个 QAndroidJniEnvironment 对象，即可获得 JNIEnv 指针，可以进一步使用 JNIEnv 的方法来实现特定功能，比如检查 JNI 调用过程中是否发生了异常、清理异常等等。</p>
<h4 data-id="heading-1">实例</h4>
<h5 data-id="heading-2">调用无参无返回值的成员函数</h5>
<p><strong>java 函数原型</strong></p>
<pre><code class="copyable">package org.qtproject.testDemo;
import android.util.Log;

public class SystemInfo  &#123;
    public static String CLASS_NAME = "SystemInfo";

    public  void exitApp()
    &#123;
        Log.i(CLASS_NAME, "exitApp");
        System.exit(0);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>QT 调用方式</strong></p>
<pre><code class="copyable">#include"QtAndroid"

QAndroidJniObject obj("org/qtproject/testDemo/SystemInfo");
obj.callMethod<void>("exitApp");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Java 的全路径类名，是带了包名的。 Java 中的包，可以类比于 C++ 里的 namespace ，一个包里可以包含了多个类，一方面方便将关联的类组织到一起，另一方面也可以避免名字冲突。当我们在 C++ 用以字符串方式描述一个 Java 类时，需要把 “.” 替换为 “/” ，如上的 <code>org/qtproject/testDemo/SystemInfo</code>，代表了 java 中的 SystemInfo 类。</p>
<h5 data-id="heading-3">调用参数为基础类型的无返回值的成员函数</h5>
<p><strong>java 函数原型</strong></p>
<pre><code class="copyable">package org.qtproject.testDemo;
import android.util.Log;

public class SystemInfo  &#123;
    public static String CLASS_NAME = "SystemInfo";

    public  void testInt(int i)
    &#123;
        Log.i(CLASS_NAME, "testInt:" + i);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>QT 调用方式</strong></p>
<pre><code class="copyable">#include"QtAndroid"

int parm = 0;
QAndroidJniObject obj("org/qtproject/testDemo/SystemInfo");
obj.callMethod<void>("testInt", "(I)V", parm);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">调用参数为对象的无返回值的成员函数</h5>
<p><strong>java 函数原型</strong></p>
<pre><code class="copyable">package org.qtproject.testDemo;
import android.util.Log;

public class SystemInfo  &#123;
    public static String CLASS_NAME = "SystemInfo";

    public  void testString(String str)
    &#123;
        Log.i(CLASS_NAME, "testString:" + str);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>QT 调用方式</strong></p>
<pre><code class="copyable">#include"QtAndroid"

QString parm = "this is QString";
QAndroidJniObject strObj = QAndroidJniObject::fromString(parm);
QAndroidJniObject obj("org/qtproject/testDemo/SystemInfo");
obj.callMethod<void>("testString","(Ljava/lang/String;)V", strObj.object<jstring>());
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">调用返回值为基础类型的成员函数</h5>
<p><strong>java 函数原型</strong></p>
<pre><code class="copyable">package org.qtproject.testDemo;
import android.util.Log;

public class SystemInfo  &#123;
    public static String CLASS_NAME = "SystemInfo";

    public int testInt_I()
    &#123;
        Log.i(CLASS_NAME, "testInt_I:void");
         return 3;
    &#125;
     public int testInt_I(int i)
    &#123;
        Log.i(CLASS_NAME, "testInt_I:" + i);
        return i;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>QT 调用方式</strong></p>
<pre><code class="copyable">#include"QtAndroid"

///无参数
QAndroidJniObject obj("org/qtproject/testDemo/SystemInfo");
const int value = obj.callMethod<jint>("testInt_I", "()I");


//参数为int
int parm = 0;
QAndroidJniObject obj("org/qtproject/testDemo/SystemInfo");
const int value = obj.callMethod<jint>("testInt_I", "(I)I", parm);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">调用返回值为对象类型的成员函数</h5>
<p><strong>java 函数原型</strong></p>
<pre><code class="copyable">package org.qtproject.testDemo;
import android.util.Log;

public class SystemInfo  &#123;
    public static String CLASS_NAME = "SystemInfo";
    String result="SystemInfo";
    
    public String testString()
    &#123;
        Log.i(CLASS_NAME, "testString");
         return result;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>QT 调用方式</strong></p>
<pre><code class="copyable">#include"QtAndroid"

///无参数
QAndroidJniObject obj("org/qtproject/testDemo/SystemInfo");
QAndroidJniObject Result = obj.callObjectMethod("testString","()Ljava/lang/String;");
qDebug() << "testString:" << Result.toString();
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">调用返回值为对象类型参数为基础类型的成员函数</h5>
<p><strong>java 函数原型</strong></p>
<pre><code class="copyable">package org.qtproject.testDemo;
import android.util.Log;

public class SystemInfo  &#123;
    public static String CLASS_NAME = "SystemInfo";
    String result="SystemInfo";
    
    public String testString_I(int i)
    &#123;
        Log.i(CLASS_NAME, "testString" + i);
        return result;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>QT 调用方式</strong></p>
<pre><code class="copyable">#include"QtAndroid"

int pram = 3;
QAndroidJniObject obj("org/qtproject/testDemo/SystemInfo");
QAndroidJniObject Result = obj.callObjectMethod("testString","(I)Ljava/lang/String;",pram);
qDebug() << "testString:" << Result.toString();
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">调用返回值为对象类型参数为对象类型的成员函数</h5>
<p><strong>java 函数原型</strong></p>
<pre><code class="copyable">package org.qtproject.testDemo;
import android.util.Log;

public class SystemInfo  &#123;
    public static String CLASS_NAME = "SystemInfo";
    String result="SystemInfo";
    
    public String testString(String str)
    &#123;
        Log.i(CLASS_NAME, "testString" + str);
        return str;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>QT 调用方式</strong></p>
<pre><code class="copyable">#include"QtAndroid"

QAndroidJniObject obj("org/qtproject/testDemo/SystemInfo");
QString param = "this is android";
QAndroidJniObject paramobj = QAndroidJniObject::fromString(param);
QAndroidJniObject Result = obj.callObjectMethod("testString","(Ljava/lang/String;)Ljava/lang/String;",paramobj.object<jstring>();
qDebug() << "testString:" << Result.toString();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            