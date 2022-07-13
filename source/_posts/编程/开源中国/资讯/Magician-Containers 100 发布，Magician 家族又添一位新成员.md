
---
title: 'Magician-Containers 1.0.0 发布，Magician 家族又添一位新成员'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8691'
author: 开源中国
comments: false
date: Wed, 13 Jul 2022 10:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8691'
---

<div>   
<div class="content">
                                                                    
                                                        <p>最近在使用Magician开发项目的过程中，发现了一些问题，有时候想对某些方法做监听，或者 想启动一个定时任务做轮询，会比较麻烦一点，因为Magician暂时没有对应的解决方案，但是 我又不想在现有的Magician里添加功能，因为这样会让项目变得越来越大，最后逐渐变成一个大胖子，失去灵活性，开发者在使用的时候，不管需不需要的功能 都会被一股脑的引入到项目中，这是我无法接受的。 而且也违背了Magician一开始的初衷，所以最后我们决定以一个新组建的形式来发布。 把用不用的权利交给用户。</p> 
<h2>Magician-Containers 带来了什么</h2> 
<ol> 
 <li>Bean管理（没有IOC，只是为了在bean上面绑定功能，解决一些麻烦）</li> 
 <li>AOP</li> 
 <li>定时任务</li> 
</ol> 
<h2>Bean管理</h2> 
<p>在类上面加一个注解即可，不可以用在controller上，也不是所有的类都需要变成一个bean，开发者可以随意决定。</p> 
<p>我们推荐，在你需要在这个类里面使用AOP或者定时任务的时候，才把它变成一个bean。</p> 
<pre><code class="language-java">@MagicianBean
public class DemoBean &#123;

&#125;</code></pre> 
<h2>AOP</h2> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">编写 AOP 的逻辑</p> 
<pre><code class="language-java">public class DemoAop implements BaseAop &#123;

    /**
     * 方法执行前
     * @param args 方法的参数
     */
    public void startMethod(Object[] args) &#123;

    &#125;

    /**
     * 方法执行后
     * @param args 方法的参数
     * @param result 方法的返回数据
     */
    public void endMethod(Object[] args, Object result) &#123;

    &#125;

    /**
     * 方法出异常后
     * @param e 方法的异常信息
     */
    public void exp(Throwable e) &#123;

    &#125;
&#125;</code></pre> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">挂到需要监听的方法上</p> 
<pre><code class="language-java">@MagicianBean
public class DemoBean &#123;

    @MagicianAop(className = DemoAop.class)
    public void demoAopMethod() &#123;

    &#125;
&#125;</code></pre> 
<h2>定时任务</h2> 
<p>目前只支持 按照间隔轮询，还不支持cron表达式</p> 
<pre><code class="language-java">@MagicianBean
public class DemoBean &#123;

    // loop: 轮询频率，单位：毫秒
    @MagicianTimer(loop=1000)
    public void demoTimerMethod() &#123;

    &#125;
&#125;</code></pre> 
<h2>获取bean对象</h2> 
<p>不可以在定义成员变量的时候直接赋值，下面示例是我们推荐的一种写法，具体可以看官网的文档</p> 
<pre><code class="language-java">@MagicianBean
public class DemoBean &#123;

    private DemoBean demoBean;

    public void demoMethod() &#123;
        demoBean = BeanUtil.get(DemoBean.class);
    &#125;
&#125;</code></pre> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">启动时加载资源</h2> 
<pre><code class="language-java">HttpServer httpServer = Magician
        .createHttp()
        .scan("com.test"); // Scanning range (package name)

// 在scan方法执行后，才可以加载bean，顺序一定要注意
MagicianContainers.load();

httpServer.bind(8080);</code></pre> 
<p>访问官网了解更多：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmagician-io.com" target="_blank">https://magician-io.com</a></p>
                                        </div>
                                      
</div>
            