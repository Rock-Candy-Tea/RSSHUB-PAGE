
---
title: 'Martian 4.0，架构大幅调整'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4818'
author: 开源中国
comments: false
date: Sat, 17 Apr 2021 17:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4818'
---

<div>   
<div class="content">
                                                                                            <h2>Martian4.0 是啥</h2> 
<p>Martian4.0 是一个 最新的主线版本，内部架构产生了巨大的变化，之前的版本 里面大部分功能都是Martian自带的，属于一个高度内聚的项目。而从4.0开始 不再以这种方式进行开发了。</p> 
<p>而是基于Magician开发，定位成一个Magician项目的超集，<span style="background-color:#ffffff; color:#24292e">整合了Magician的大部分组件，并进行了少量的二次封装，使其可以快捷的构建后端服务。</span></p> 
<p><span style="color:#24292e">4.x 将会跟 3.x 并行维护，一直到3.x的用户都转到4.x 为止。</span></p> 
<h2><span style="background-color:#ffffff; color:#24292e">4.0 带来了哪些变化</span></h2> 
<h3><span style="background-color:#ffffff; color:#24292e">一、AOP与IOC没了</span></h3> 
<p><span style="background-color:#ffffff; color:#24292e">为什么会这样的呢？ 因为Magician没有这两个特性，所以Martian自然也不会有了，加是可以加的，但是考虑到几个问题所以暂时不打算支持。</span></p> 
<p>首先，IOC 和 new的区别 在于，IOC的对象是框架创建的，所以这个对象上可以被框架绑定很多功能，AOP就是其中一项，但是在实际开发中，IOC的作用体现的不是很明显，甚至很多场景都不需要IOC，尤其是注解式开发流行以后，IOC的优势就大大下滑了。</p> 
<p>AOP，一般用的最多的就是 做声明式事务，其他场景很少用，而Magician 有类似的组件可以实现声明式事务，所以AOP 也不是特别的刚需了，如果真的需要可以自己用动态代理实现。</p> 
<h3>二、不再内置Jedis</h3> 
<p>Jedis是redis的Java客户端，其本身已经封装的够强了，个人认为没必要再套个壳子了。比如，想要连接操作redis，只需要这样。</p> 
<pre><code class="language-java">JedisPool jedisPool = new JedisPool(连接池, url,
                    端口, 超时时间,
                    用户名, 密码,
                    库索引, 是否ssl);

Jedis jedis = jedisPool.getResource();</code></pre> 
<p>这个代码量 跟之前Martian封装过相比，相差并不大（连配置的代码也一起算上）。而且还不用专门学习怎么在Martian中连接redis，只需要直接用原生Jedis即可。</p> 
<p>如果未来Magician 出了封装Jedis的模块，那么到时候会集成进来。</p> 
<h3>三、Controller支持路由配置</h3> 
<p>之前都是直接请求方法名的，现在由于是基于Magician开发的，所以Controller也支持路由自定义了，但是声明式API没了，不再支持。</p> 
<pre><code class="language-java">@Route("/demoController")
public class DemoController &#123;

    @Route(value = "/demo", requestMethod = ReqMethod.POST)
    public DemoVO demo(DemoVO demoVO)&#123;
        return demoVO;
    &#125;
&#125;</code></pre> 
<h3>四、定时任务没了</h3> 
<p>因为没了IOC所以 与其绑定的功能 自然也都没了。不过自己写也不难，JDK自带了定时任务的api。</p> 
<pre><code class="language-java">// 2000毫秒执行一次
Timer timer = new Timer();  
timer.schedule(new TimerTask() &#123;  
     public void run() &#123;  
         System.out.println("-------设定要指定任务--------");  
     &#125;  
&#125;, 2000);// 设定指定的时间time,此处为2000毫秒</code></pre> 
<p>后面会开发定时任务相关的组建，来弥补这个缺失。</p> 
<h4>五、暂时与Martian-cloud，Martian-gateway不兼容</h4> 
<p>考虑到项目规模太小，不太可能有人在用Martian开发微服务，所以这两个组件暂时不考虑兼容，后面再进行迭代</p> 
<h2>3.x 以后还会继续维护吗</h2> 
<p>当然会继续维护，不过 基本会以修bug为主，不再提供新功能了。一直维护到所有用户都转到了4.x为止。</p> 
<p>而且大家也不用担心，4.x 不会简简单单的基于Magician的，后面会持续迭代，出更多功能的。其使用的便捷程度不会低于3.x，甚至会高于3.x。</p> 
<p>而且Magician一旦出了新组建，将会被快速集成到Martian的。</p> 
<h2>Magician是啥</h2> 
<p>可以看这个官网了解一下哦：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmagician-io.com%2F" target="_blank">http://magician-io.com</a></p>
                                        </div>
                                      
</div>
            