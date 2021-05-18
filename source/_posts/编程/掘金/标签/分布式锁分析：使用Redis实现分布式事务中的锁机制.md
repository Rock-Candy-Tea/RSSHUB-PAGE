
---
title: '分布式锁分析：使用Redis实现分布式事务中的锁机制'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=1172'
author: 掘金
comments: false
date: Sun, 16 May 2021 20:02:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=1172'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">分布式协调服务</h1>
<ul>
<li>Zookeeper是分布式协调服务框架</li>
<li><strong>分布式协调技术:</strong> 主要用来解决分布式环境当中多个进程之间的同步控制,让进程有序的去访问某种临界资源,防止造成"脏数据"的后果</li>
<li>分布式协调技术的<strong>核心</strong>就是实现<strong>分布式锁</strong></li>
</ul>
<h1 data-id="heading-1">分布式锁</h1>
<ul>
<li><strong>分布式锁:</strong> 为了防止分布式系统中的多个进程之间相互干扰,需要分布式协调技术对进程进行调度,这个分布式协调技术的核心就是实现分布式锁</li>
</ul>
<h3 data-id="heading-2">分布式锁条件</h3>
<ul>
<li>在分布式系统环境下,一个方法在同一时间只能被一个机器的一个线程执行</li>
<li>高可用的获取锁与释放锁</li>
<li>高性能的获取锁与释放锁</li>
<li>具备可重入特性</li>
<li>具备锁失效机制,防止死锁</li>
<li>具备非阻塞锁特性</li>
</ul>
<h3 data-id="heading-3">分布式锁的实现</h3>
<ul>
<li><strong>Zookeeper</strong></li>
<li><strong>Redis</strong></li>
<li><strong>Memcached</strong></li>
<li><strong>Chubby</strong></li>
</ul>
<h1 data-id="heading-4">Redis分布式锁的实现</h1>
<ul>
<li>分布式锁实现的三个核心要素:加锁,解锁,锁超时</li>
<li>Redis是单线程的</li>
</ul>
<h3 data-id="heading-5">加锁</h3>
<ul>
<li>使用setnx命令</li>
<li>key是锁的唯一标识,按业务来决定命名</li>
<li>value可以设置成任意值</li>
<li>当一个线程执行setnx返回1,说明key原本不存在,该线程成功得到锁.当一个线程执行setnx返回0,说明key已经存在,该线程抢锁失败</li>
</ul>
<h3 data-id="heading-6">解锁</h3>
<ul>
<li>当得到锁的线程执行完任务,需要释放锁,以便其它线程可以进入,使用del指令释放锁之后,其它线程就可以继续执行setnx命令获得锁</li>
</ul>
<h3 data-id="heading-7">锁超时</h3>
<ul>
<li>一个得到所得线程在执行任务的过程中出现问题,不能显式释放锁,这些资源将永远被锁住,造成死锁的状态</li>
<li>setnx的key要设置一个超时时间,保证锁没有被显式释放时,会在一定时间后自动释放.setnx不支持超时参数,需要额外的指令expire</li>
</ul>
<hr>
<ul>
<li><strong>Redis分布式锁问题:</strong>
<ul>
<li>非原子性操作:
<ul>
<li><strong>解决方案:</strong> 通过使用set命令<strong>set(key,value,expire)</strong> 设置为原子操作</li>
</ul>
</li>
<li>误删锁:
<ul>
<li>在设置锁超时的情况下,操作没有完成,当操作完成时,del命令删除的是其它进程的锁</li>
<li><strong>解决方案:</strong> 判断是否为本进程的锁.带着key和<strong>value=threadID</strong>线程ID判断是否为本进程的锁</li>
</ul>
</li>
<li>在设置锁超时的情况下,操作没有完成
<ul>
<li><strong>解决方案:</strong> 释放锁时判断操作是否完成, <strong>增加守护线程:为锁超时加时,延迟释放</strong></li>
</ul>
</li>
</ul>
</li>
</ul></div>  
</div>
            