
---
title: 'ZQPool 1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7761'
author: 开源中国
comments: false
date: Wed, 06 Jul 2022 16:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7761'
---

<div>   
<div class="content">
                                                                                            <p>ZQPool是一个可以替代pgbouncer的连接池软件。主要解决PostgreSQL生态中流行的连接池软件pgbouncer软件的一些缺点。</p> 
<p>通常使用数据库连接池的主要目的有两个：</p> 
<ol> 
 <li>减少到数据库上的连接数。应用程序到连接池软件上有M个连接，这M个连接不是同时都繁忙的，这M个连接上同一个时刻发来的并发SQL可能只有N个（N通常大大小于M)，这样连接池软件只需要在后端数据库上建N个连接。就可以满足了要求。这个场景通常是java应用。 我们可以想象一个场景：一个java应用可能部署在200台主机上，而每个主机上java应用自身会开启一个java连接池，这个java连接池假设开20个连接，这时到数据库上就有200*20=4000个连接，这些连接实际上多数时间都是空闲的，少数时间才是活跃的。 4000个连接，PostgreSQL数据库就需要启动4000个进程，太多连接会降低数据库的效率。</li> 
 <li>减少短连接应用花在新建数据库连接的时间。PostgreSQL数据库对每一个连接需要fork出一个新的进程来提供服务，而每次fork一个进程是需要时间的。而连接池软件可以预先建好到数据库的连接，应用程序连接到连接池软件后，连接池软件可以从池中取一个已经建好的连接马上提供服务，这样就大大减少了新连接的时间。这个场景的典型应用是php应用。php应用到数据库通常是短连接。</li> 
</ol> 
<p>而PostgreSQL数据库中流行的pgbouncer通常解决不了上面的第一个问题（java应用）：即减少到数据库上连接数的目的。 要减少到数据库上的连接数，pgbouncer连接池的模式只能配置成语句级或事务级，不能配置成会话级，因为pgbouncer在会话级下，前面来多少个连接，到数据库也必须建多少连接，根本起不到减少数据库连接的目的。当我们把pgbouncer配置成语句级或事务级时，java应用连接pgbouncer会报错: </p> 
<pre><code class="language-java">org.postgresql.util.PSQLException: ERROR: prepared statement "S_1" already exists </code></pre> 
<p> </p> 
<p>这个原因是jdbc执行SQL是分两个步骤的:</p> 
<ol> 
 <li>先使用Prepare的SQL，即：“prepare S_1 as select * from test01 where id=$1;” </li> 
 <li> 然后再“execute S1(1);”</li> 
</ol> 
<p>报错的原因为：</p> 
<ol> 
 <li>执行“prepare S_1 as select * from test01 where id=$1;”时，从连接池中取一个连接A，执行后，就释放了此连接；</li> 
 <li>执行“execute S_1(1);”，再从连接池中获得一个连接，这时获得的连接可能已经不是之前的连接，这个新连接中没有Prepare语句“S_1”，所以就报错了；</li> 
 <li>如果又来了另一个SQL，可能从连接池中取到的还是之前的连接A，然后再执行“prepare S_1 as select * from test02 where id=$1;”，但这个prepare SQL 的名字S_1已经被前面的SQL占用，这时就报错了。</li> 
 <li>当然jdbc的实际行为比上面描述的要复杂的多，但原理大致就是上面描述的这个过程。</li> 
</ol> 
<p>而ZQPool通过跟踪一个连接上的Prepare SQL的名字，并替换成不重复的名字的方式解决了这个问题。</p> 
<p>pgbouncer还有一个缺点，处理SQL的转发只能用到CPU的一个核，即pgbouncer是单线程程序。对于高并发的情况下，超过单核的性能时，就会立即出现瓶颈。而ZQPool是使用golang的协程技术，可以利用了多核的性能，在一台2颗 Intel(R) Xeon(R) Silver 4210R CPU @ 2.40GHz的物理机：</p> 
<p>这是pgbouncer的测试情况：</p> 
<pre><code class="language-bash">[postgres@csyun01 ~]$ pgbench -h 10.197.160.18 -p 6432 -Uu01  -S -P 2  -T 30 -c 32
pgbench (14.3)
starting vacuum...end.
progress: 2.0 s, 30407.5 tps, lat 1.050 ms stddev 0.180
progress: 4.0 s, 30108.6 tps, lat 1.062 ms stddev 0.182
progress: 6.0 s, 30231.5 tps, lat 1.058 ms stddev 0.179
progress: 8.0 s, 31157.9 tps, lat 1.026 ms stddev 0.176
progress: 10.0 s, 30491.7 tps, lat 1.049 ms stddev 0.178
progress: 12.0 s, 30463.0 tps, lat 1.050 ms stddev 0.180
progress: 14.0 s, 30366.2 tps, lat 1.053 ms stddev 0.179
progress: 16.0 s, 30177.5 tps, lat 1.060 ms stddev 0.180
progress: 18.0 s, 30067.1 tps, lat 1.064 ms stddev 0.181
progress: 20.0 s, 30420.1 tps, lat 1.051 ms stddev 0.177
...
...
...</code></pre> 
<p> </p> 
<p>这是使用ZQPool测试的情况：</p> 
<pre><code class="language-bash">[postgres@csyun01 ~]$ pgbench -h 10.197.160.18 -p 5436 -Uu01  -S -P 2  -T 30 -c 32
Password:
pgbench (14.3, server 10.5)
starting vacuum...end.
progress: 2.0 s, 111134.7 tps, lat 0.213 ms stddev 0.058
progress: 4.0 s, 112688.1 tps, lat 0.209 ms stddev 0.058
progress: 6.0 s, 114570.8 tps, lat 0.207 ms stddev 0.054
progress: 8.0 s, 107305.3 tps, lat 0.216 ms stddev 0.066
progress: 10.0 s, 108680.1 tps, lat 0.215 ms stddev 0.063
progress: 12.0 s, 108867.6 tps, lat 0.214 ms stddev 0.064
...
...
...
</code></pre> 
<p>可以看到ZQPool的tps可以到10万每秒，而pgbouncer最多到3万每秒就上不去了。</p>
                                        </div>
                                      
</div>
            