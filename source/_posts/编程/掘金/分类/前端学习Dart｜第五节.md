
---
title: '前端学习Dart｜第五节'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d13dbe7593824d7086b1d309e06cfa83~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 18:30:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d13dbe7593824d7086b1d309e06cfa83~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>本章节主要讲解知识点：Map对象、dart:convert、MapEntry、Javascript Map、自平衡二叉树</p>
<p>视频地址：<a href="https://www.bilibili.com/video/BV1Ff4y1a7xy/" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p>
<h2 data-id="heading-1">Map</h2>
<p>Map对象是一个简单的键/值对，Map是动态集合。换句话说，Maps可以在运行时增长和缩小。</p>
<p>可以通过两种方式声明Map</p>
<ul>
<li>使用Map构造函数</li>
<li>使用Map字面量</li>
</ul>
<h2 data-id="heading-2">构造器声明</h2>
<p>Map对象可以使用构造器如下声明</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d13dbe7593824d7086b1d309e06cfa83~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">字面量声明</h2>
<p>Map对象使用字面量声明如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa38e19ed13d421e896bcd4e89c653a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">修改操作</h2>
<p>构造函数初始化方式:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d995b9d54e964646bfddf25ebac285ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述两种声明方式都可以以如下方法初始化Map对象</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba42548c02994080aac33dcd57398c30~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在Map键值对中，其中的“键”，也就是K，可以为任意类型(这里可以称为对象，因为所有类型都是对象)，包括null。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eafb15671ce1468d8aeca72ec366a297~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上赋值了两个类型的key, Map对象类型、null。都是可以的。</p>
<p>这里可能需要提前了解一下var，还记得在最开始章节讲var的时候使用var声明变量，在Dart编译过程中会进行类型推断，在Map类型中也是这样的。但是有一点点不同，因为Map对象有两种类型：key，value</p>
<p>看一下这个例子：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e94a12eff38e44f48a49ea88c3f95302~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Dart 会将 a 的类型推断为 Map<String, String>， 如果尝试在上面的 map 中添加错误类型，那么分析器或者运行时会引发错误。其余的知识点将在泛型章节讲解。提前预知一下。</p>
<h2 data-id="heading-5">常用属性及方法</h2>
<h3 data-id="heading-6">Map.from()</h3>
<p>克隆一个 Map，通过 Map.from() 仅仅能够实现浅克隆。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba6b1a0fe90b4610bf71c47764621061~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于深克隆，我们可以简单的这样去处理:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b03c2a89c79e4c67ba146c79cef41e66~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">dart: convert</h4>
<p>解码(JSON String->Object)</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39a9555c63c440b38f80d02255aafff0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编码(Object->JSON String): 支持int, double, String, bool, null, List, Map (with string keys)</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/413c7ed6823342adb91a8a667255cb2a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解码(UTF-8)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1a686080c5403b8d4fe1fe67a45bf4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编码(UTF-8)</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe6dd241eb8d46d9a985193b137ae412~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">fromIterable()</h3>
<p>从Iterable类型生成Map对象</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72c5707b494a4baea235e44e6838ec82~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">fromIterables()</h3>
<p>从两个Iterable类型生成Map对象，一个为key参照，一个为value参照。两个Iterable类型长度必须一致。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80982433bc8e47348274527d36de1286~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">keys</h3>
<p>获取所有的keys，根据上一节课讲解的List对象理论来讲，这里返回的keys也是Iterable类型，并不是直接返回List对象类型。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a2103a29f7045da9cc31a7f95e6213d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">values</h3>
<p>获取所有的values，返回Iterable类型</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1357ca7318e74e20986486f91c5200f6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">isEmpty</h3>
<p>判断Map对象是否为空</p>
<h3 data-id="heading-13">remove()</h3>
<p>删除指定key的数据</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dadb8ffcaf84be19d0686f9078a5d7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">addAll()</h3>
<p>合并指定Map对象</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7e1b95ab1cf429c9bd3451c91938861~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">containsValue()</h3>
<p>判断在Map对象中是否有指定的值，返回bool类型</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc89bfd9313449c5b81ca69e5b207160~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">containsKey()</h3>
<p>判断在Map对象中是否有指定的key，返回bool类型</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83806f39dc3949adaa7c652b0bd6bbbf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">length</h3>
<p>返回在map中键值对的数量</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aecddffe07484582b6f86e2ffc490b41~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">forEach()</h3>
<p>循环map中的键值对，内部函数参数分别为key、value，函数为void 无返回值</p>
<p>forEach循环中不可以删除或修改key的值</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7ea73bcb3844e52b5e7639859cea4f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">updateAll()</h3>
<p>根据函数规则更新所有的<code>值</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7ed1232d68e4111976815ce9bc9c5c5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">map</h3>
<p>语法：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9eb9449010384ea48e551840722d3c56~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>map() 遍历每个键值对 根据参数函数，对key、value做出修改，转换成其他Map。转换的Map可以是其他类型。</p>
<h2 data-id="heading-21">MapEntry</h2>
<p>创建一条键值对，也可以说为一条键值对的表示。我们先确定一下概念，Map对象是键值对的集合，是个集合。MapEntry表示一条键值对。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bbe42c953d84a6c9f20baa2dafc64cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然MapEntry有自己的属性及方法：key、value等.</p>
<p>多个MapEntry即为entries。看一下语法</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dc77ea1dc5848e78967b8eaf3ecc672~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可知entries为Iterable类型。单个MapEntry意义不大，多个必须为Iterable类型。这样的话方便迭代。</p>
<h3 data-id="heading-22">fromEntries()</h3>
<p>也可以通过多个MapEntry生成Map对象</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd34fd6ebdef4bb7b7f10454ca90b099~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么Iterable类型转换成Map类型后，同样的forEach难道都是Iterable 的forEach？</p>
<p>是的，只不过迭代顺序概念上有些区别</p>
<p>List：迭代按照索引顺序。</p>
<p>Map：</p>
<ul>
<li>普通的hashMap是无序的</li>
<li>LinkedHashMap迭代顺序为key插入的顺序</li>
<li>SplayTreeMap 自平衡二叉树中的 - 伸展树🌲</li>
</ul>
<p>Map对象的迭代顺序属于第二种。</p>
<h2 data-id="heading-23">自平衡二叉树</h2>
<p>这个东西没有百度百科讲的好，直接看视频：<a href="https://baike.baidu.com/item/%E5%B9%B3%E8%A1%A1%E6%A0%91/7641279?fr=aladdin" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p>
<p>那么Dart中的SplayTreeMap是什么样的呢：</p>
<p>对于经常存储和访问的数据（如缓存），SplayTreeMap是一个不错的选择。 原因是他们使用树旋转将一个元素调到根，以便更频繁地访问。 性能来自树的自我优化。 也就是说，频繁访问的元素移动到更靠近顶部。 但是，如果同时经常访问树，那么使用SplayTreeMap几乎没有意义。</p>
<p>举个例子，调制解调器路由器以非常高的速率接收网络数据包。 调制解调器必须决定哪个数据包进入哪个线路。 这可以使用map实现，其中键是IP，值是目标线路。 对于这种情况，SplayTreeMap是一个不错的选择，因为大多数IP地址将被多次使用，因此可以从树的根目录找到它们。</p>
<h2 data-id="heading-24">javascript Map</h2>
<h3 data-id="heading-25">Object</h3>
<blockquote>
<p>Properties are identified using key values</p>
</blockquote>
<p>javascript中的Object本质上解为键值对的集合，</p>
<p>键的话只可以为字符串或者Symbol值。Symbol类型的key在上一节课的时候讲到了一个Symbol.iterator。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7aab8d3c31649f9be3961b055a9b2d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这本身会有很大的限制。所以为了解决这个问题，ES6 提供了 Map 数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。也就是说，Object 结构提供了“字符串—值”的对应，Map 结构提供了“值—值”的对应。如果你需要“键值对”的数据结构，Map 比 Object 更合适。</p>
<h3 data-id="heading-26">Map</h3>
<p>javascript中的Map大家都比较了解，这里讲解一点。</p>
<p>Map.keys在javascript中返回的依然是迭代协议。上面Dart Map对象中的keys返回为Iterable类型，这里与Iterable章节内容相呼应。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/755590946fdd4403a7286a4bb8392693~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>javascript中Map的遍历顺序就是插入顺序。</p>
<h2 data-id="heading-27">END</h2>
<p>本章节主要讲解知识点：Map对象、dart:convert、MapEntry、Javascript Map、自平衡二叉树。</p></div>  
</div>
            