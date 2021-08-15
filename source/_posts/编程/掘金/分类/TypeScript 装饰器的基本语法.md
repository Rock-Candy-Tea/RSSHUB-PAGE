
---
title: 'TypeScript 装饰器的基本语法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a80fd9b742aa4e18aff7479f53cca3ed~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 01:47:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a80fd9b742aa4e18aff7479f53cca3ed~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>相信大家一定在很多代码中见过这样的用法：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a80fd9b742aa4e18aff7479f53cca3ed~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对，没错像 <strong>@classDecorator</strong> <strong>、****@propertyDecorator</strong> 这样子的语法就是装饰器。</p>
<h2 data-id="heading-0">装饰器是什么</h2>
<p>要解释装饰器是什么，这里引用官方文档中一句话：</p>
<blockquote>
<p>Decorators provide a way to add both annotations and a meta-programming syntax for class declarations and members</p>
</blockquote>
<p>装饰器就是一种<strong>为类和类的成员添加注解或者实现元数据编程的语法</strong>。</p>
<p>来看个具体的例子，在这个例子中 <strong>@classDecorator</strong> 就是一个类的装饰器：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ce443dcc1cd4058b57e5ad9b28f9d28~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出：装饰器本质很简单，它就是一个函数，加上**@**符号，被应用到一些特定的目标上，就实现一个装饰器。</p>
<p><strong>装饰器仅在解释执行时运行一次。</strong></p>
<blockquote>
<p>Decorators will be called at runtime with information about the decorated declaration.</p>
</blockquote>
<h3 data-id="heading-1">装饰器工厂</h3>
<p>说到这里，需简单介绍一下另一种非常常见的创建装饰器的方式：<strong>装饰器工厂（Decorator Factories）</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66523a87a2034a0fb4904fa86084e8b7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个时候，我们添加装饰器的时候不再是 <strong>@classDecorator</strong> 而是执行了这个函数 <strong>@classDecorator()</strong></p>
<p>而<strong>函数执行返回的函数才是真正的装饰器本身。</strong></p>
<p>这种用法多用于装饰器需要根据用户传参来表现出不同的能力的场景。</p>
<blockquote>
<p>If we want to customize how a decorator is applied to a declaration, we can write a decorator factory.</p>
</blockquote>
<p>当然也有同学会单纯的喜欢这样的写法。</p>
<h2 data-id="heading-2">TypeScript 中有哪些装饰器</h2>
<p>在 TypeScript 中，可以实现以下五种装饰器：<strong>类装饰器、方法装饰器、属性装饰器、访问器装饰器、参数装饰器</strong></p>
<h3 data-id="heading-3">类装饰器</h3>
<p>类装饰器声明于类之前</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a4283aa88154f75a9d2831b4eb93efe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>类装饰器仅有<strong>一个参数</strong>：</p>
<ul>
<li>类的构造器（<strong>Player</strong>）</li>
</ul>
<p><strong>返回值</strong>：可以返回一个类来替代你所装饰的类（可选）。例如：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a420e09e765f4857bf490098712a8dd4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样一来，所有的 <strong>Player</strong> 其实已经变成了 <strong>Swimmer</strong>。当你 <strong>new Player()</strong> 得到其实是 <strong>Swimmer</strong> ，不过在 TS 的类型系统中存在一个问题，它并不会帮你识别这个实例是 <strong>Swimmer</strong> 类型。详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fdecorators.html%23class-decorators" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/decorators.html#class-decorators" ref="nofollow noopener noreferrer">这里</a>。</p>
<h3 data-id="heading-4">方法装饰器</h3>
<p>方法装饰器声明于类的方法之前，包括<strong>实例方法</strong>和<strong>静态方法</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f42050bebd48410286ee4cdbffcf3326~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>方法装饰器有<strong>三个参数</strong>：</p>
<ul>
<li>
<p>如果是<strong>静态方法</strong>就是类的构造器（<strong>Player</strong>），如果是<strong>实例方法</strong>就是类的原型（<strong>Player.prototype</strong>）</p>
</li>
<li>
<p>函数名</p>
</li>
<li>
<p>函数的属性描述符</p>
</li>
</ul>
<p><strong>返回值</strong>：可以将其属性描述符返回（可选）</p>
<h3 data-id="heading-5">属性装饰器</h3>
<p>属性装饰器申明于类的属性之前，包括<strong>实例属性</strong>和<strong>静态属性</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bfde2f47d024b4fa4e49a58e4b797ab~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>属性装饰器有<strong>两个参数</strong>：</p>
<ul>
<li>如果是<strong>静态方法</strong>就是类的构造器（<strong>Player</strong>），如果是<strong>实例方法</strong>就是类的原型（<strong>Player.prototype</strong>）</li>
<li>属性名</li>
</ul>
<p><strong>返回值</strong>：Void</p>
<h3 data-id="heading-6">访问器装饰器</h3>
<p>访问器装饰器申明于类的访问器（<strong>get/set</strong>）之前，包括<strong>实例访问器</strong>和<strong>静态访问器</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ec13341041f4e4eb7c6686b1170b986~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>访问器装饰器有<strong>三个参数</strong>：</p>
<ul>
<li>
<p>如果是<strong>静态方法</strong>就是类的构造器（<strong>Player</strong>），如果是<strong>实例方法</strong>就是类的原型（<strong>Player.prototype</strong>）</p>
</li>
<li>
<p>属性名</p>
</li>
<li>
<p>访问器属性的属性描述符</p>
</li>
</ul>
<p><strong>返回值</strong>：可以将其属性描述符返回（可选）</p>
<p><strong>注意</strong>：对于同一个属性来讲，<strong>不能同时在 get/set 上都是用装饰器，只需要选择一个即可</strong></p>
<h3 data-id="heading-7">参数装饰器</h3>
<p>参数装饰器申明于类方法的参数之前，包括<strong>实例方法</strong>和<strong>静态方法</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76747831dc39479cb397c1a4fc63cdca~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>参数装饰器有<strong>三个参数</strong>：</p>
<ul>
<li>
<p>如果是<strong>静态方法</strong>就是类的构造器（<strong>Player</strong>），如果是<strong>实例方法</strong>就是类的原型（<strong>Player.prototype</strong>）</p>
</li>
<li>
<p>参数名</p>
</li>
<li>
<p>参数是函数参数列表的第几个</p>
</li>
</ul>
<p><strong>返回值</strong>：Void</p>
<h2 data-id="heading-8">多种装饰器的执行顺序</h2>
<p>在了解了所有的装饰器类型后，这里存在的一个问题就是：如果多种装饰器被任意组合在一起，执行顺序是怎么的呢？我们直接来看一个例子：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbd0b959a3d24736a79a32cf04182d61~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了方便我们自定义输出信息，这里全部使用了装饰器工厂的实现，例如：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/016d57fc651b43d69c8e01049006a29b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个包含了所有类型装饰器的例子，其执行结果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac4944fc312b43a69d5683b8c78471f2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>更多的相关内容可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fdecorators.html%23decorator-evaluation" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/decorators.html#decorator-evaluation" ref="nofollow noopener noreferrer">官方文档</a></p>
<h2 data-id="heading-9">对同一个属性的装饰器组合</h2>
<p>对于同一个属性，TypeScript 允许我们为它应用多个装饰器，就像这样：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04131218b72e4e3faccdc33a911696e9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其执行顺序为：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a201d94e04b04dee94e9aad743fdd4e2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，装饰器本身是按照距离被装饰目标从近到远的顺序执行的，等同于 <strong>f(g(getValue()))</strong></p>
<p>如果使用的是装饰器工厂的话，像这样</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f9d21c5ebfe48429c835fd78c449b96~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其执行顺序为：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a64a5f3bd7b4bdd8dbfe1922734de76~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>更多的相关内容可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fdecorators.html%23decorator-composition" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/decorators.html#decorator-composition" ref="nofollow noopener noreferrer">官方文档</a>。</p>
<h2 data-id="heading-10">总结</h2>
<p>这篇文档的主要目的就是想要说明 TypeScript 的装饰器语法是什么样子的，以及需要注意的事项，希望能够帮助大家在使用的时候，上手快一点，不要踩坑。</p>
<p>至于装饰器为什么会是这样个样子，以及在很多场景下的典型应用，后续通过其他的文章分享给大家。</p>
<h2 data-id="heading-11">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fdecorators.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/decorators.html" ref="nofollow noopener noreferrer">TypeScript Decorator 官方文档</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsaul-mirone.github.io%2Fa-complete-guide-to-typescript-decorator%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://saul-mirone.github.io/a-complete-guide-to-typescript-decorator/" ref="nofollow noopener noreferrer">A Complete Guide to TypeScript Decorators</a>（非常推荐）</li>
</ul></div>  
</div>
            