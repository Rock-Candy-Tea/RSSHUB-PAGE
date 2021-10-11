
---
title: '事件领域模型框架 kaka 基础核心 kaka-core 更新至 4.0 稳定版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6889'
author: 开源中国
comments: false
date: Mon, 11 Oct 2021 16:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6889'
---

<div>   
<div class="content">
                                                                    
                                                        <p>kaka 是一项<span>服务于 Java 后端的事件领域模型，全局事件通知框架。</span></p> 
<p>kaka-core已移至 <a href="https://gitee.com/zkpursuit/kaka-core">https://gitee.com/zkpursuit/kaka-core</a> ， 并支持 maven 直接安装。</p> 
<p><strong>此次更新主要强化和稳定以下两个功能点：</strong></p> 
<p>1、单个事件对应多个 Command，3.0版本之前仅支持一个 Command 对应多个事件。在此基础上同名事件对应的 Command 新增执行优先级，可依此模拟切面编程，以下代码为模拟切面方法拦截器，获取主体业务执行耗时。</p> 
<pre><code class="language-java"><span><span>//基于事件模拟切面编程，仅支持Command</span></span>
sendMessage(<span><span>new</span></span> Message(<span><span>"40000"</span></span>), <span><span>true</span></span>);</code></pre> 
<pre><code class="language-java"><span><span>package</span></span> kaka.test.unit;

<span><span>import</span></span> com.kaka.notice.Command;
<span><span>import</span></span> com.kaka.notice.Message;
<span><span>import</span></span> com.kaka.notice.annotation.Handler;

<span><span>/**
 * 模拟切面
 */</span></span>
<span><span>@Handler</span></span>(cmd = <span><span>"40000"</span></span>, type = String<span><span>.</span><span><span><span>class</span></span></span><span>, </span><span><span><span>priority</span></span></span><span> </span></span>= <span><span>2</span></span>)
<span><span>public</span></span> <span><span><span><span>class</span></span></span><span> </span><span><span><span>SimulateAopCommand</span></span></span><span> </span><span><span><span>extends</span></span></span><span> </span><span><span><span>Command</span></span></span><span> </span></span>&#123;
    <span><span>@Override</span></span>
    <span><span><span><span>public</span></span></span><span> </span><span><span><span>void</span></span></span><span> </span><span><span><span>execute</span></span></span><span><span><span>(Message msg)</span></span></span><span> </span></span>&#123;
        <span><span>try</span></span> &#123;
            Thread.sleep(<span><span>2000</span></span>);
        &#125; <span><span>catch</span></span> (InterruptedException e) &#123;
            e.printStackTrace();
        &#125;
        System.out.println(<span><span>"Aop业务执行"</span></span>);
    &#125;
&#125;</code></pre> 
<pre><code class="language-java"><span><span>package</span></span> kaka.test.unit;

<span><span>import</span></span> com.kaka.notice.Command;
<span><span>import</span></span> com.kaka.notice.IResult;
<span><span>import</span></span> com.kaka.notice.Message;
<span><span>import</span></span> com.kaka.notice.SyncResult;
<span><span>import</span></span> com.kaka.notice.annotation.Handler;

<span><span>/**
 * 模拟切面，执行前
 */</span></span>
<span><span>@Handler</span></span>(cmd = <span><span>"40000"</span></span>, type = String<span><span>.</span><span><span><span>class</span></span></span><span>, </span><span><span><span>priority</span></span></span><span> </span></span>= <span><span>1</span></span>)
<span><span>public</span></span> <span><span><span><span>class</span></span></span><span> </span><span><span><span>SimulateAopBeforeCommand</span></span></span><span> </span><span><span><span>extends</span></span></span><span> </span><span><span><span>Command</span></span></span><span> </span></span>&#123;
    <span><span>@Override</span></span>
    <span><span><span><span>public</span></span></span><span> </span><span><span><span>void</span></span></span><span> </span><span><span><span>execute</span></span></span><span><span><span>(Message msg)</span></span></span><span> </span></span>&#123;
        IResult execStartTime = <span><span>new</span></span> SyncResult<>(); <span><span>//中间变量亦可使用 ThreadLocal 存储</span></span>
        execStartTime.set(System.currentTimeMillis());
        msg.setResult(<span><span>"execStartTime"</span></span>, execStartTime);
    &#125;
&#125;</code></pre> 
<pre><code class="language-java"><span><span>package</span></span> kaka.test.unit;

<span><span>import</span></span> com.kaka.notice.Command;
<span><span>import</span></span> com.kaka.notice.IResult;
<span><span>import</span></span> com.kaka.notice.Message;
<span><span>import</span></span> com.kaka.notice.annotation.Handler;

<span><span>/**
 * 模拟切面，执行后
 */</span></span>
<span><span>@Handler</span></span>(cmd = <span><span>"40000"</span></span>, type = String<span><span>.</span><span><span><span>class</span></span></span><span>, </span><span><span><span>priority</span></span></span><span> </span></span>= <span><span>3</span></span>)
<span><span>public</span></span> <span><span><span><span>class</span></span></span><span> </span><span><span><span>SimulateAopAfterCommand</span></span></span><span> </span><span><span><span>extends</span></span></span><span> </span><span><span><span>Command</span></span></span><span> </span></span>&#123;
    <span><span>@Override</span></span>
    <span><span><span><span>public</span></span></span><span> </span><span><span><span>void</span></span></span><span> </span><span><span><span>execute</span></span></span><span><span><span>(Message msg)</span></span></span><span> </span></span>&#123;
        IResult execStartTime = msg.getResult(<span><span>"execStartTime"</span></span>);
        <span><span>long</span></span> offset = System.currentTimeMillis() - execStartTime.get();
        System.out.println(<span><span>"Aop业务执行耗时："</span></span> + offset);
    &#125;
&#125;</code></pre> 
<p>2、异步回调获取事件处理结果，此功能为同步获取事件处理结果的增强和优化。</p> 
<pre><code class="language-java">sendMessage(<span><span>new</span></span> Message(<span><span>"50000"</span></span>, <span><span>""</span></span>, (IResult<<span><span>Object</span></span>> result) -> &#123;
            Class clasz = ((CallbackResult<<span><span>Object</span></span>>) result).eventHanderClass;
            StringBuilder sb = <span><span>new</span></span> StringBuilder(<span><span>"异步回调：\\\\t"</span></span> + clasz.getTypeName() + <span><span>"\\\\t"</span></span>);
            <span><span>Object</span></span> resultObj = result.get();
            <span><span>if</span></span> (resultObj <span><span>instanceof</span></span> <span><span>Object</span></span>[]) &#123;
                <span><span>Object</span></span>[] ps = (<span><span>Object</span></span>[]) resultObj;
                sb.append(Arrays.toString(ps));
            &#125; <span><span>else</span></span> &#123;
                sb.append(resultObj);
            &#125;
            System.out.println(sb);
        &#125;), <span><span>true</span></span>);</code></pre> 
<p>以上范例代码均可在源码test中查阅，其中包括常用通用性范例。</p>
                                        </div>
                                      
</div>
            