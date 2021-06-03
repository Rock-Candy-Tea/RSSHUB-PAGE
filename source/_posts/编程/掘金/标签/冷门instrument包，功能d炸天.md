
---
title: '冷门instrument包，功能d炸天'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://juejin.cn/post/undefined'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 01:39:23 GMT
thumbnail: 'https://juejin.cn/post/undefined'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>文中代码示例工程如下，更多参考btrace和arthas：</p>
<pre><code class="copyable">https://github.com/sayhiai/example-javaagent
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>5版本以后，jdk有一个包叫做<code>instrument</code>，能够实现一些<strong>非常酷</strong>的功能。市面上一些<code>APM</code>工具，就是通过它来进行的增强。</p>
<p>这是基础架构的必备技能，但对业务开发来说并不是。许多面试会问到这个知识点，并不是因为将来会用到，而是因为你说对<code>jdk</code>比较熟悉，他想杀杀你的威风。</p>
<p>不会用没问题，但你要说不知道，就过分了点。</p>
<h1 data-id="heading-0">javaagent介绍</h1>
<p>我们通常的java入口都是一个<code>main</code>方法，而<code>javaagent</code>的入口方法叫做<code>premain</code>，表明是在main运行之前的一些操作。javaagent就是一个jar包，定义了一个标准的premain()方法，并不需要继承或者实现任何其他的类。</p>
<blockquote>
<p>这是一个约定，并木有什么其他的理由。这个方法，无论是第一次加载，还是每次新的ClassLoader加载，都会执行。</p>
</blockquote>
<p>我们可以在这个前置的方法里，对字节码进行一些修改，来增加功能或者改变代码的行为。这种方法没有侵入性，只需要在启动命令中加上-javaagent参数就可以。Java6以后，甚至可以通过attach的方式，动态的给运行中的程序设置加载代理类。</p>
<p>有经验的同学肯定要提出异议了。其实，instrument有两个main方法，一个是<code>premain</code>，一个是<code>agentmain</code>，在一个JVM中，只会调用一个；前者是main执行之前的修改，后者控制类运行时的行为。它们还是有一些区别的，agentmain因为比较危险，限制会更大一些。</p>
<h1 data-id="heading-1">有什么用</h1>
<h2 data-id="heading-2">获取统计信息</h2>
<p>许多apm产品，比如Pinpoint、SkyWalking等，就是使用javaagent对代码进行的增强。通过在方法执行前后动态加入的统计代码，进行监控信息的收集；通过兼容OpenTracing协议，可以实现分布式链路追踪的功能。 它的原理类似于aop，最终以字节码存在，性能损失取决于你的代码逻辑。</p>
<h2 data-id="heading-3">热部署</h2>
<p>通过自定义的ClassLoader，可以实现代码的热替换。使用agentmain，实现热部署功能会更加便捷。通过agentmain获取到Instrumentation以后，就可以对类进行动态重定义。</p>
<h2 data-id="heading-4">诊断</h2>
<p>配合<code>JVMTI</code>技术，可以<code>attach</code>到某个进程进行运行时统计和调试，比较流行的<code>btrace</code>和<code>arthas</code>，底层就是这种技术。</p>
<h1 data-id="heading-5">如何做</h1>
<p>大体分为以下步骤：</p>
<ul>
<li>构建agent jar包，编写增强代码</li>
<li>在manifest中指定Premain-Class/Agent-Class属性</li>
<li>使用参数加载或者attach方式使用</li>
</ul>
<h2 data-id="heading-6">编写Agent</h2>
<p>javaagent最终的体现方式是一个jar包。使用idea创建一个默认的maven工程即可。</p>
<p>创建一个普通java类，添加<code>premain</code>或者<code>agentmain</code>方法，它们的参数完全一样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d5c54b81b1b465eb380b7973aa0984a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h2 data-id="heading-7">编写Transformer</h2>
<p>此部分，要借助额外jar包的功能。</p>
<p>实际的代码逻辑需要实现<code>ClassFileTransformer</code>接口。假如我们要统计某个方法的执行时间。我们使用<code>javaassist</code>来增强字节码，则可以通过以下代码来实现。</p>
<ul>
<li>获取<code>MainRun</code>类的字节码实例</li>
<li>获取<code>hello</code>方法的字节码实例</li>
<li>在方法前后，加入时间统计，首先定义变量<code>_begin</code>，然后直接编写代码</li>
</ul>
<p>别忘了加入maven依赖</p>
<pre><code class="copyable"><dependency>
    <groupId>org.javassist</groupId>
    <artifactId>javassist</artifactId>
    <version>3.24.1-GA</version>
</dependency>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/699a626ee37048769d7aba25f84a6a99~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​ 字节码增强也可以使用Cglib、asm等其他工具。</p>
<h2 data-id="heading-8">MANIFEST.MF文件</h2>
<p>那么我们编写的代码是如何让外界知晓呢？那就是<code>MANIFEST.MF</code>文件。具体路径在 src/main/resources/META-INF/MANIFEST.MF</p>
<pre><code class="copyable">Manifest-Version: 1.0
premain-class: com.sayhiai.example.javaagent.AgentApp
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>一般的，maven打包会覆盖这个文件，所以我们需要指定需要哪一个。</p>
<pre><code class="copyable"><build><plugins><plugin>
<groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-jar-plugin</artifactId>
    <configuration>
        <archive>
            <manifestFile>src/main/resources/META-INF/MANIFEST.MF</manifestFile>
            </archive>
    </configuration></plugin></plugins></build>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>然后，在命令行，执行<code>mvn install</code>安装到本地代码库，或者使用<code>mvn deploy</code>发布到私服上。</p>
<p>附，MANIFEST.MF参数清单： Premain-Class Agent-Class Boot-Class-Path Can-Redefine-Classes Can-Retransform-Classes Can-Set-Native-Method-Prefix</p>
<h2 data-id="heading-9">使用</h2>
<p>使用方式取决于你使用的premain还是agentmain。</p>
<h3 data-id="heading-10">premain</h3>
<p>直接在启动命令行中加入参数即可，在jvm启动时启用代理。</p>
<pre><code class="copyable">java -javaagent:agent.jar MainRun
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>在idea中，可以将参数附着在jvm options里。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93c260038c114c67bfce445a613a7115~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>接下来看一下测试代码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/949d5d2361314798918b41e8b872c7f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这是我们的执行类。执行后，直接输出hello world。通过增强以后，还额外的输出了执行时间，以及一些debug信息。其中，debug信息在main方法执行之前输出。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e132739aecd480f91002832e9caa417~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h2 data-id="heading-11">agentmain</h2>
<p>一般用在一些诊断工具上。使用jdk/lib/tools.jar中的功能，可以动态的为运行中的程序加入功能。主要有以下步骤：</p>
<ul>
<li>获取机器上运行的所有jvm的进程id</li>
<li>选择要诊断的jvm</li>
<li>将jvm使用attach函数链接上</li>
<li>使用loadAgent函数加载agent，动态修改字节码</li>
<li>卸载jvm</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eeec72a8cad493f9388f32ca2ab3b6b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这些代码都是比较危险的，这就是为什么Btrace说了这么多年，还是只在小范围内被小心使用。相对来说，arthas显的友好而且安全的多。</p>
<h1 data-id="heading-12">注意点</h1>
<h2 data-id="heading-13">一、jar包依赖方式</h2>
<p>一般，agent的jar包会以fatjar的方式提供，即将所有的依赖打包到一个大的jar包中。</p>
<p>如果你的功能复杂，依赖多，那么这个jar包将会特别的大。</p>
<p>使用独立的bom文件维护这些依赖是另外一种方法。使用方自行管理依赖问题，但这通常会发生一些找不到jar包的错误。更糟糕的是，大多数在运行时才发现。</p>
<h2 data-id="heading-14">二、类名称重复</h2>
<p>不要使用和jdk以及instrument包中相同的类名（包括包名)，有时候你能够侥幸过关，但也会陷入无法控制的异常中。</p>
<h2 data-id="heading-15">三、做有限的功能</h2>
<p>可以看到，给系统动态的增加功能是非常酷的，但大多数情况下非常耗费性能。你会发现，一些简单的诊断工具，占用你1核的cpu，是稀松平常的事情。</p>
<h2 data-id="heading-16">四、ClassLoader</h2>
<p>如果你用的jvm比较旧，频繁的生成大量的代理类，会造成perm区的膨胀，容易发生OOM。</p>
<p>ClassLoader有双亲委派机制，如果你想要替换相应的类，一定要搞清楚它的类加载器应该用哪个。否则替换的类，是不生效的哦。</p>
<h1 data-id="heading-17">End</h1>
<p>将你的增强代码，加入类似zk的主动通知功能，可以通过管理后台动态的调整应用的行为。如果再集成一个类似groovy的脚本语言，理论上，你能够干任何事情。</p>
<p>所以，使用<code>-javaagent</code>参数引入的<code>jar</code>包，或者使用<code>attach</code>方式提供的一些诊断工具，小姐姐都不敢随便的用。</p>
<h1 data-id="heading-18">可关注我的B站账号→→→→<a href="https://space.bilibili.com/618498318" target="_blank" rel="nofollow noopener noreferrer">B站账号</a></h1>
<h1 data-id="heading-19">学习交流群→→→→<a href="https://docs.qq.com/doc/DVURTSlpDZUJxVlNM" target="_blank" rel="nofollow noopener noreferrer">交流群</a></h1></div>  
</div>
            