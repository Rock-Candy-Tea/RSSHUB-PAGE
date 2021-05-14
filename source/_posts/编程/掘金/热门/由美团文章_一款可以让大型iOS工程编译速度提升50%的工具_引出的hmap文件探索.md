
---
title: '由美团文章_一款可以让大型iOS工程编译速度提升50%的工具_引出的.hmap文件探索'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d40ebb6f820b4e129166c3de17e30244~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 05 May 2021 08:24:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d40ebb6f820b4e129166c3de17e30244~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d40ebb6f820b4e129166c3de17e30244~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>系列文章：<a href="https://juejin.im/post/6871441300521304077" target="_blank" rel="nofollow noopener noreferrer">OC底层原理系列</a>，<a href="https://juejin.im/post/6889028196704976910" target="_blank" rel="nofollow noopener noreferrer">OC基础知识系列</a>，<a href="https://juejin.cn/post/6914837339353120775" target="_blank">Swift底层探索系列</a>，<a href="https://juejin.cn/post/6923957462714286093" target="_blank">iOS高级进阶系列</a></strong></p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>前段时间，同事给我推荐了一篇美团的文章：<a href="https://juejin.cn/post/6934554272142983181" target="_blank">一款可以让大型iOS工程编译速度提升50%的工具</a>，一看标题就觉得惊讶，为什么呢？因为它<code>能让编译速度提示50%</code>，我们日常的<code>提升编译速度</code>就是将<code>组件编译成二进制文件导入项目</code>，但是它的<code>提升</code>也<code>没有这么多</code>。本着不清楚的就去了解的原则，就来看看怎么实现的。</p>
<h1 data-id="heading-1">探索</h1>
<h2 data-id="heading-2">编译耗时原因</h2>
<p>在项目中我们会引入头文件，例如下图：我们<code>在ViewController中引入了Person的头文件</code>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58978e71bdaf4684962c0c7035b83a50~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在我们<code>引入头文件</code>的时候，引入的是<code>头文件的名称Person</code>，那么Xcode是怎么找到这个Person文件实际位置的呢？这就要提到<code>项目中配置的header search path</code>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61e5ca51320d4e1cb0164912bb87ac1b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>Xcode</code>在<code>编译</code>的<code>时候</code>会<code>读取到header search path的地址</code>，并且<code>拼接</code>上我们<code>引入的头文件名</code>。</p>
<p>也就意味着我们导入的<code>头文件</code>分成<code>两个部分</code>：</p>
<ul>
<li>1.<code>前半部分</code>：<code>头文件所在的文件目录</code></li>
<li>2.<code>后半部分</code>：<code>头文件名称</code></li>
</ul>
<p>这也就是为什么我们设置header search path的时候，<code>只需要设置头文件所在目录就可以</code>了。</p>
<p>问题：因为我们<code>项目里有很多文件</code>，那么我们就会<code>在header search path设置很多目录</code>，但是对于找到我们上面<code>引入一个头文件Person</code>，他需要<code>查找遍历所有</code>的<code>文件目录</code>，来<code>找到这个类</code>。这个<code>过程随着项目的类越来越多</code>，<code>查找</code>的<code>时间</code>就会<code>越来越长</code>，就会<code>越来越耗时</code>。比如我们项目组件多达上百个，类有上万个，那么这个过程所产生的的耗时就比较明显了。</p>
<h2 data-id="heading-3">解决办法</h2>
<p>上面我们知道项目编译耗时的原因，那么怎么解决这个问题呢？美团的文章给出答案，就是<code>使用hmap</code></p>
<h3 data-id="heading-4">hmap</h3>
<p>hmap是什么呢？美团文章说了它<code>就是Header Map的实体</code>，类似于一个<code>Key-Value的形式</code>，<code>Key值</code>是<code>头文件</code>的<code>名称</code>，<code>Value</code>是<code>头文件</code>的<code>实际物理路径</code>，其实这个东西<code>一直都存在</code>，只不过我们没注意到罢了。</p>
<ul>
<li>大家想一下，<code>第一次</code>运行项目或者编译的时候，会发现<code>很慢</code>，但是一旦<code>运行</code>或者<code>编译成功</code>后，<code>再次编译</code>或者<code>运行</code>就会<code>很快</code>，想过为什么没？</li>
<li>其实<code>第一次编译后</code>，<code>Xcode</code>就<code>会</code>帮我们<code>生成一些.hmap文件</code>，<code>再次编译</code>时候会<code>直接使用</code>这些<code>.hmap文件快速找到</code>对应的<code>头文件</code>，所以编译速度就会快很多</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe3eae8654634d89a4e16a7bce5f324e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们看到<code>生成</code>了<code>很多.hmap文件</code>，<code>Xcode</code>是<code>按类别生成</code>的，<code>箭头指</code>的就是<code>我们主项目工程</code>的<code>.hmap文件</code>，如果我们<code>对Xcode进行清理</code>，那么这些<code>.hmap文件</code>也会<code>被清掉</code>，然后我们就会发现，<code>编译又慢</code>了起来。</p>
</blockquote>
<p>通过上面的讲解我们知道<code>.hmap</code>其实就<code>是个容器</code>，它<code>内部</code>肯定<code>包含</code>了<code>Person</code>的<code>文件目录</code>，那么就会<code>让</code>我们<code>Xcode</code>在<code>查找Person</code>的<code>头文件</code>时<code>更快</code>速，那么有个问题就出来了，我们自己<code>怎么去生成.hmap文件</code>呢？<code>.hmap</code>的<code>底层结构</code>又是怎样的呢？</p>
<h2 data-id="heading-5">探究.hmap文件</h2>
<p>我们编译一个项目，查看编译过程，找到ViewController.m文件
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bedb29ffbe64811b63df4d5ca3393b2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我用<code>红[]括住</code>，我们可以看到它是用<code>-I参数</code>去<code>引入了一个.hmap文件</code>，上面我们也知道<code>Xcode</code>会<code>生成多个.hmap</code>，为了方便大家理解我们需要<code>读取下.hmap文件</code></p>
</blockquote>
<h3 data-id="heading-6">.hmap文件结构分析</h3>
<p>先看下项目目录
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2000c51787864d99b99731482b5c83c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们再看下<code>这个项目生成的.hmap</code>是什么文件格式
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2275e7b26704b338bfa600628980e41~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们发现这个里面<code>包含了项目里所有的.h</code>，下面我们来看看<code>.hmap</code>究竟<code>是什么样的数据结构</code></p>
</blockquote>
<ul>
<li>数据结构</li>
</ul>
<p>我们可以通过LLVM来查找相关的内容
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7255d269f3f548d89f374e872b31bbd3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们看到有个<code>结构体叫HMapHeader</code>，还有个<code>结构体叫HMapBucket</code>，红框有两句话：1.<code>有一个NumBuckets的HMapBucket对象数组紧跟在这个头文件后面</code>。2.<code>有个字符串跟随在HMapBucket后面，在StringsOffset</code></p>
</blockquote>
<p>通过上面我们可以猜测一下.hmap的结构
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45c90f33575b44c8aef6274f9c6b81e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1.<code>最上面的HMapHeader，记录一些必要信息</code></li>
<li>2.<code>中间的HMapBucket，有多少个头文件，就会有多少个HMapBucket，这些都会包装成HMapBucket</code></li>
<li>3.<code>字符串里就是包含着头文件的前半部分路径以及后半部分类名的字符串</code></li>
</ul>
<blockquote>
<p>流程：通过<code>读取HMapHeader</code>，<code>获取.hmap保存了多少个Bucket</code>，也就知道了这个<code>.hmap保存</code>了<code>多少</code>个<code>头文件路径</code>，而<code>Bucket里保存</code>了这个<code>头文件在下面字符串中的偏移量</code>，然后就可以<code>从最下面的字符串</code>中<code>读取到该头文件的路径</code></p>
</blockquote>
<h3 data-id="heading-7">读取.hmap文件</h3>
<p>我们怎么读取.hmap信息呢？上面<code>从LLVM</code>中我们<code>找到hmap的有关结构信息</code>，那么在LLVM里面是否有存取相关内容呢？</p>
<ul>
<li>上面我们知道<code>结构体信息</code>是<code>在Lex文件下</code>找到，那么读取信息是不是也在Lex中</li>
<li>最后我找到一个<code>HeaderMapTest</code>的<code>文件</code>，感觉是<code>测试HeaderMap的文件</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01539faef024495f9750b4683e6e7ef0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们在<code>读取hmap时</code>，需要用到<code>上面的结构体</code></p>
</blockquote>
<p>下面我们就来用LLVM获取的信息，写一个<code>读取HeaderMap的插件</code>（我们在main文件中写）</p>
<h4 data-id="heading-8">hmap读取</h4>
<p>我们在main函数中写如下代码：</p>
<ul>
<li>断言宏</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43beed08ea1a4fe2b92e8cc14b37094b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>HMAP_HeaderMagicNumber</code>是<code>字符串翻转</code>，因为<code>在HMapHeader结构体</code>中<code>有个属性Magic来表示字节顺序</code>，也就是说<code>如果当前的Magic=HMAP_SwappedMagic</code>，也就意味着<code>字节顺序是反转</code>的，也就<code>需要重新交换下字节顺序</code></p>
</blockquote>
<ul>
<li>2.参数判断非正常文件</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de3325377a674ad3a78e27868478033d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>当参数小于两个的时候</code>（说明没有传什么东西）这个时候就<code>认为是无效</code>的</p>
</blockquote>
<ul>
<li>3.正常文件</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/435b46c2c5f148918a5d2dc4a38c6d23~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>循环通过dump方法导出header map</code></p>
</blockquote>
<h4 data-id="heading-9">dump方法</h4>
<p>这个方法我是<code>使用C</code>来写的，因为感觉<code>C在处理取文件时更方便些</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f2da990820048dc969baae1c898c949~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>传进来的是<code>文件路径</code></p>
</blockquote>
<ul>
<li>1.<code>解析路径</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e4b4a5384e04e5687f5d554f88c1b1e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>解析</code>的<code>路径长度小于0</code>说明路径<code>不正常</code></p>
</blockquote>
<ul>
<li>2.<code>获取MapHeader大小并判断</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa4829d9aa90468689b0213af3b187e7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>拿到<code>MapHeader大小</code>，如果<code><0</code>则<code>说明MapHeader异常</code>，如果<code>小于实际的MapHeader大小</code>，则说明<code>读取</code>的<code>数据异常</code></p>
</blockquote>
<ul>
<li>3.<code>判断字符串是否翻转，读取header</code></li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/248a33fd7ff94dbda6a58af2d293b18c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4.<code>获取桶的数目</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5966d73518a04d948ce866306cbe8900~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>5.<code>获取桶的数组</code>（指针偏移）</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/125dd7517c814b5bbd11abe2c2178e50~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>6.<code>获取String列表</code>（指针偏移）</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b67ae540b6d843a9b402d8b062bab9a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>6.<code>遍历获取桶</code>，然后<code>取出桶</code>的<code>前缀</code>和<code>后缀进行拼接</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1cb9130dd7f4fa89be6b1fe37d7a303~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
上面我们就把一个<code>读取.hmap的代码写好</code>了，下面将之前的项目的.hmap代码放到这个项目目录里，然后在下图进行设置
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec02c3e8affe4496938a84206e5e7265~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">运行项目，打断点</h4>
<ul>
<li>1.main函数断点</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7f3f61dba6e42a2b293e9bc17f33b99~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>第一个是<code>当前可执行文件</code>的<code>路径</code>，第二个是<code>刚才配置的.hmap路径</code></p>
</blockquote>
<ul>
<li>2.查看桶数目</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16d812a74e7b41b6bb47c0994ec75834~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>打印是<code>16个桶</code>，但是<code>不都是头文件地址</code>（由于<code>数据对齐</code>的原因）</p>
</blockquote>
<ul>
<li>3.查看打印数据</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d4d452d5d742ff80e5fed3d8b97cdc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>String表有9个数据</code>，<code>bucket数目有16个</code></p>
</blockquote>
<ul>
<li>4.查看结果</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/089b054e031a488daa02b5f89ff728fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">总结</h4>
<p>通过上面的读取打印我们可以确认一下几点：</p>
<ul>
<li>1.上面说的<code>.hmap是一个key-value形式</code>，<code>key是头文件名</code></li>
<li>2.<code>prefix保存的是头文件路径的前半部分</code></li>
<li>3.<code>suffix保存的是头文件路径的后半部分</code>（头文件名）</li>
<li>4.<code>.hmap是按照对应规则存储的一堆头文件</code></li>
</ul>
<p>也证明了上面我们的猜想是对的</p>
<h4 data-id="heading-12">扩展</h4>
<p>上面写的代码可以生成一个工具，我们把<code>工具添加</code>到我们的<code>lldb执行命令里</code>，这样我们就不用上面的方式读取.hmap文件，我们就可以在<code>终端使用命令一样读取</code>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38b4ca4e755d4832a7d8cdd2d03d7b7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">生成自己的.hmap文件</h2>
<p>上面说了<code>xcode</code>自己就能<code>主动</code>帮我们<code>生成.hmap文件</code>，那为什么还需要我们自己写呢？美团的文章里说了，这里我再简单的说下：</p>
<ul>
<li>1.我们的项目一般都会<code>通过cocoaPods来管理第三方</code>，比如我之前没事写的Swift项目引入下面的第三方库</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3b39309cdcc4c5a9c71c6f6698d31ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>2.上面我们发现<code>以#import "ClassA.h"形式的头文件</code>，才会<code>命中.hmap文件</code>，<code>否则都将通过Header Search Path寻找其相关路径</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357048bd39d843c4a6d40ab511feae3d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>目录的问题上面说过<code>它会在多个目录里查找一个头文件是比较耗时</code>，那么如果我把<code>一个文件路径放到一个.hmap文件中</code>，那就回<code>快很多</code>。此时如果<code>引入的组件和第三方比较多</code>，那么<code>势必会导致编译速度慢</code>。</p>
</blockquote>
<h3 data-id="heading-14">写代码生成自己的.hmap文件</h3>
<p>这部分也是个难点，本人也是查看了上面提到的<code>LLVM中的HeaderMapTest.cpp文件</code>，仔细看了下代码，发现里面有些<code>生成.hmap代码</code>，自己写的<code>代码比较的简单</code>，就是为了<code>说明.hmap是如何生成</code>的</p>
<ul>
<li>1.上面介绍<code>.hmap文件</code>说到，里面<code>包含很多的Bucket</code>，所以我们要<code>先生成Bucket</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a91344d71394d06ae01bcfa07d17e7f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>创建MapFile容器Maker</code>，Maker中包含<code>一个个MapFile</code>，也就是<code>Bucket</code>，<code>MapFile是一个结构体</code>（HeaderMapTest.cpp中一样，其中的<code>8代表多少个Bucket</code>，<code>750是生成buffer的大小</code>）</p>
</blockquote>
<ul>
<li>2.核心代码，将<code>类名</code>和<code>路径以Bucket</code>的<code>形式保存</code>
<ul>
<li>方法总览
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0bf9d5d099a48d18e409e642eebcae7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>addString方法
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8692dbef96740209afdd8953c5e0963~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>addBucket方法<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59a3b33cacd24f0aa16df313df68d360~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
</li>
</ul>
<blockquote>
<p>上面的方法都是<code>从LLVM的HeaderMapTest.cpp中找到的</code></p>
</blockquote>
<ul>
<li>3.将文件导出指定位置
<ul>
<li>方法总览
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/380370c83d014b53bcf8e9137f6799f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>getBuffer方法<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dff84f2d929a431db99378847aca9c21~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
</li>
<li>4.运行项目</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6989ba2150834f8fb13cc6800e1f4646~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>生成了一个<code>TestApp.hmap文件</code>，下面我们来<code>读取</code>下这个文件，看看和Xcode生成的是否一样</p>
</blockquote>
<ul>
<li>5.读取生成的TestApp.hmap</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d694fbce7de24091886538be2d24757c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
和Xcode生成的.hmap
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38b4ca4e755d4832a7d8cdd2d03d7b7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们发现<code>生成</code>的<code>结果</code>是<code>一样</code>的，下面我们就去使用下这个自己生成.hmap</p>
</blockquote>
<ul>
<li>6.使用自己生成.hmap</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81397de0856645258fd5b1dfeaf77440~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>将Use Header Maps设置为NO，<code>将Header Search Paths路径设置成我们生成的.hmap路径</code>。由于<code>写的项目工程太小，测不出来太大的差别</code>。</p>
</blockquote>
<h1 data-id="heading-15">总结</h1>
<p>上面讲了.hmap的读写方法，看完也就.hmap有个比较清晰的认识了，<code>美团文章解决编译速度的思路值得我们去学习</code>，我上面<code>生成.hmap</code>的<code>方法</code>其实<code>无法落地</code>的，就是为了给大家说一下<code>怎么去生成一个.hmap</code>，<code>美团文章里说</code>的<code>cocoapods-hmap-prebuilt这个插件</code>，我<code>个人感觉是一个脚本</code>，<code>遍历头文件脚本</code>。上面说的<code>生成.hmap方法无法落地</code>，如果让它<code>能够落地</code>，就是<code>写一个脚本</code>去<code>遍历项目</code>以及<code>cocoapods管理</code>的<code>第三方库</code>的<code>头文件</code>，<code>将头文件提取出来</code>，<code>用上面</code>的<code>方法</code>，最后<code>生成</code>一个<code>.hmap文件</code>，这样<code>才能落地</code>。这部分也作为自己的一个技术探索吧，后面有了结果再给大家分享</p></div>  
</div>
            