
---
title: 'iOS-屏幕适配（Masonry）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=1444'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 19:35:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=1444'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看： <a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h3 data-id="heading-0">Masonry简介</h3>
<p><strong><code>Masonry</code>是一个轻量级的布局框架，拥有自己的描述语法，采用更优雅的链式语法封装<code>AutoLayout</code>，简洁明了并具有高可读性，而且同时支持 iOS 和 Max OS X</strong></p>
<p><strong>下载链接 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSnapKit%2FMasonry" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SnapKit/Masonry" ref="nofollow noopener noreferrer">Masonry</a></strong></p>
<hr>
<h3 data-id="heading-1">Masonry配置</h3>
<ul>
<li>使用pods方式引入类库，<code>pod 'Masonry'</code></li>
<li>引入头文件 <code>#import "Masonry.h"</code></li>
</ul>
<hr>
<h3 data-id="heading-2">Masonry使用</h3>
<p><strong>示例：</strong></p>
<pre><code class="hljs language-js copyable" lang="js">[testView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
        
     make.left.mas_equalTo(self.view.mas_left).offset(<span class="hljs-number">50</span>);
     make.right.mas_equalTo(self.view.mas_right).offset(-<span class="hljs-number">50</span>);           
     make.top.mas_equalTo(self.view.mas_top).offset(<span class="hljs-number">50</span>);
     make.bottom.mas_equalTo(self.view.mas_bottom).offset(-<span class="hljs-number">50</span>);
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>基本格式：（<code>make . </code>指定其的一个属性<code>.</code>约束关系）</strong></p>
<pre><code class="hljs language-js copyable" lang="js">make.attr.constrains
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>make</code>:可认为是要布局的<code>view</code>的代理</p>
<p><code>constrains</code>:约束可能是多级的组合，比如<code>.mas_equalTo(self.view.mas_left).offset(50)</code>的两级组合，显示找到父<code>view</code>的左边位置，再向右（X轴）移动50点</p>
<h3 data-id="heading-3">给控件添加、更新约束</h3>
<ul>
<li>
<p>添加新的约束</p>
<pre><code class="hljs language-js copyable" lang="js">[xxxView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
     
  &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>删除控件以前所有约束，添加新约束</p>
<pre><code class="hljs language-js copyable" lang="js">[xxxView mas_remakeConstraints:^(MASConstraintMaker *make) &#123;
      
  &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>更新约束，写哪条更新哪条，其他约束不变</p>
<pre><code class="hljs language-js copyable" lang="js">[xxxView mas_updateConstraints:^(MASConstraintMaker *make) &#123;
      
  &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<pre><code class="copyable">关于更新约束布局相关的API，主要用以下四个API：
-(void)updateConstraintsIfNeeded调用此方法，如果有标记为需要重新布局的约束，则立即进行重新布局，内部会调用updateConstraints方法
-(void)updateConstraints重写此方法，内部实现自定义布局过程
-(BOOL)needsUpdateConstraints当前是否需要重新布局，内部会判断当前有没有被标记的约束
-(void)setNeedsUpdateConstraints标记需要进行重新布局
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">关于UIView重新布局相关的API，主要用以下三个API：
-(void)setNeedsLayout标记为需要重新布局
-(void)layoutIfNeeded查看当前视图是否被标记需要重新布局，有则在内部调用layoutSubviews方法进行重新布局
-(void)layoutSubviews重写当前方法，在内部完成重新布局操作
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">设置约束关系</h3>





























<table><thead><tr><th align="center">约束关系</th><th align="center">说明</th></tr></thead><tbody><tr><td align="center"><code>equalTo()</code> 和 <code>mas_equalTo()</code></td><td align="center">设置属性等于某个数值</td></tr><tr><td align="center"><code>greaterThanOrEqualTo()</code> 和 <code>mas_ greaterThanOrEqualTo()</code></td><td align="center">设置属性大于或等于某个数值</td></tr><tr><td align="center"><code>lessThanOrEqualTo()</code> 和 <code>mas_ lessThanOrEqualTo()</code></td><td align="center">设置属性小于或等于某个数值</td></tr><tr><td align="center"><code>multipliedBy()</code> 和 <code>mas_ multipliedBy()</code></td><td align="center">设置属性乘以因子后的值</td></tr><tr><td align="center"><code>dividedBy()</code> 和 <code>mas_ dividedBy()</code></td><td align="center">设置属性除以因子后的值</td></tr></tbody></table>
<h3 data-id="heading-5">设置控件布局属性</h3>

























<table><thead><tr><th align="center">布局属性</th><th align="center">说明</th></tr></thead><tbody><tr><td align="center">尺寸</td><td align="center"><code>width</code>、<code>height</code>、<code>size</code></td></tr><tr><td align="center">边距</td><td align="center"><code>left</code>、<code>top</code>、<code>right</code>、<code>bottom</code>、<code>leading</code>、<code>trailing</code></td></tr><tr><td align="center">中心点</td><td align="center"><code>center</code>、<code>centerX</code>、<code>centerY</code></td></tr><tr><td align="center">边界</td><td align="center"><code>edges</code></td></tr></tbody></table>
<pre><code class="copyable">
//iOS8之后Masonry新出了几个属性：
//距离边框的距离，等同于选中Storyboard的Constrain to margins后加约束
@property (nonatomic, strong, readonly) MASConstraint *leftMargin;
@property (nonatomic, strong, readonly) MASConstraint *rightMargin;
@property (nonatomic, strong, readonly) MASConstraint *topMargin;
@property (nonatomic, strong, readonly) MASConstraint *bottomMargin;
@property (nonatomic, strong, readonly) MASConstraint *leadingMargin;
@property (nonatomic, strong, readonly) MASConstraint *trailingMargin;
@property (nonatomic, strong, readonly) MASConstraint *centerXWithinMargins;
@property (nonatomic, strong, readonly) MASConstraint *centerYWithinMargins;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>leading</code>与<code>left</code>，<code>trailing</code>与<code>right</code> 在正常情况下是等价的，但是当一些布局是从右至左时(比如阿拉伯文) 则会对调</p>
<h3 data-id="heading-6">关于mas_xxx和xxx的比较</h3>
<ul>
<li>
<p>以<code>equalTo()</code> 和 <code>mas_equalTo()</code>为例</p>
<pre><code class="copyable">#define mas_equalTo(...)                 equalTo(MASBoxValue((__VA_ARGS__)))
#define mas_greaterThanOrEqualTo(...)      greaterThanOrEqualTo(MASBoxValue((__VA_ARGS__)))
#define mas_lessThanOrEqualTo(...)       lessThanOrEqualTo(MASBoxValue((__VA_ARGS__)))

#define mas_offset(...)                  valueOffset(MASBoxValue((__VA_ARGS__)))
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>默认情况下</li>
</ul>
<p><code>equalTo()</code>：参数支持的类型除了<code>NSNumber</code>之外，还有<code>CGPoint</code> <code>CGSize</code> <code>UIEdgeInsets</code>
<code>mas_equalTo()</code>：对其参数进行了一个<code>Auto Boxing</code>操作(装箱) <code>MASBoxValue</code>(根据传入参数类型的不同，装箱成 <code>NSValue</code> 或 <code>NSNumber</code> 类型的对象)，对参数并不挑剔，几乎是传啥数据类型都可以</p>
<ul>
<li>
<p>对于对象或是多个属性的处理，使用<code>equalTo</code>。特别是多个属性时，必须使用<code>equalTo</code></p>
</li>
<li>
<p>添加下面的宏（必须加在 <code>#import "Masonry.h"</code> 前面）</p>
<pre><code class="hljs language-js copyable" lang="js">#define MAS_SHORTHAND_GLOBALS
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码里<code>mas_equalTo</code>可以不加<code>mas</code>前缀，<code>mas_equalTo</code>和<code>equalTo</code>没有区别</p>
<pre><code class="hljs language-js copyable" lang="js">[redView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
    make.width.equalTo(<span class="hljs-number">100</span>);
    make.height.mas_equalTo(<span class="hljs-number">100</span>);        
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>以<code>width()</code> 和 <code>mas_width()</code>为例</p>
<ul>
<li>
<p>默认情况下
<code>width()</code>：<code>make</code>对象的一个属性，用来添加宽度约束，表示对宽度进行约束</p>
</li>
<li>
<p><code>mas_width()</code>：一个属性值，用来当做<code>equalTo</code>的参数，表示某个控件的宽度属性</p>
</li>
<li>
<p>添加下面的宏（必须加在 <code>#import "Masonry.h"</code> 前面）</p>
<pre><code class="hljs language-js copyable" lang="js">#define MAS_SHORTHAND   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码里<code>mas_width</code>可以不加<code>mas</code>前缀</p>
<pre><code class="hljs language-js copyable" lang="js">[redView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
 make.left.mas_equalTo(self.left).offset(<span class="hljs-number">10</span>);
 make.top.mas_equalTo(self.top).offset(<span class="hljs-number">10</span>);
 make.right.mas_equalTo(self.right).offset(-<span class="hljs-number">10</span>);
 make.bottom.mas_equalTo(self.bottom).offset(-<span class="hljs-number">10</span>);
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-7">设置约束偏移</h3>






























<table><thead><tr><th align="center">方法</th><th align="center">参数</th><th align="center">说明</th></tr></thead><tbody><tr><td align="center"><code>offset(CGFloat offset)</code></td><td align="center"><code>CGFloat</code></td><td align="center">控件属性相对于参照物偏移多少</td></tr><tr><td align="center"><code>centerOffset(CGPoint offset)</code></td><td align="center"><code>CGPoint</code></td><td align="center">控件<code>center</code>相对于参照物的偏移大小</td></tr><tr><td align="center"><code>sizeOffset(CGSize offset)</code></td><td align="center"><code>CGSize</code></td><td align="center">控件<code>size</code>相对于参照物偏移多少</td></tr><tr><td align="center"><code>insets(MASEdgeInsets insets)</code></td><td align="center"><code>MASEdgeInsets</code></td><td align="center">控件四边相对于参照物偏移多少</td></tr></tbody></table>
<p><code>offset</code>示例</p>
<pre><code class="hljs language-js copyable" lang="js">[redView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
           make.left.mas_equalTo(self.mas_left).offset(<span class="hljs-number">20</span>);
           make.top.mas_equalTo(self.mas_top).offset(<span class="hljs-number">20</span>);
           make.right.mas_equalTo(self.mas_right).offset(-<span class="hljs-number">20</span>);
           make.bottom.mas_equalTo(self.mas_bottom).offset(-<span class="hljs-number">20</span>);
 &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>centerOffset</code>示例</p>
<pre><code class="hljs language-js copyable" lang="js">[redView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
        make.size.mas_equalTo(<span class="hljs-number">100</span>);
        make.center.equalTo(self).centerOffset(CGPointMake(-<span class="hljs-number">100</span>, -<span class="hljs-number">100</span>));
 &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>sizeOffset</code>示例</p>
<pre><code class="hljs language-js copyable" lang="js">[redView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
        make.center.mas_equalTo(self);
        make.width.and.height.mas_equalTo(self).sizeOffset(CGSizeMake(-<span class="hljs-number">40</span>, -<span class="hljs-number">40</span>));
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>insets</code>示例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//具体父控件四周都是20间距</span>
[redView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
       make.edges.mas_equalTo(self).insets(UIEdgeInsetsMake(<span class="hljs-number">20</span>, <span class="hljs-number">20</span>, <span class="hljs-number">20</span>, <span class="hljs-number">20</span>));
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">设置约束优先级</h3>
<ul>
<li><code>Masonry</code>为我们提供了三个默认的方法，<code>priorityLow()</code>、<code>priorityMedium()</code>、<code>priorityHigh()</code>，优先级最大数值是1000
<pre><code class="hljs language-js copyable" lang="js"> typedef UILayoutPriority MASLayoutPriority;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> MASLayoutPriority MASLayoutPriorityRequired = UILayoutPriorityRequired;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> MASLayoutPriority MASLayoutPriorityDefaultHigh = UILayoutPriorityDefaultHigh;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> MASLayoutPriority MASLayoutPriorityDefaultMedium = <span class="hljs-number">500</span>;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> MASLayoutPriority MASLayoutPriorityDefaultLow = UILayoutPriorityDefaultLow;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">const</span> MASLayoutPriority MASLayoutPriorityFittingSizeLevel = UILayoutPriorityFittingSizeLevel;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>自己设置优先级的值，可以通过<code>priority()</code>方法来设置
<pre><code class="hljs language-js copyable" lang="js">[redView mas_makeConstraints:^(MASConstraintMaker *make) &#123;
      
      make.center.mas_equalTo(self.view);
      make.width.mas_equalTo(<span class="hljs-number">100</span>).priorityLow();
      make.width.mas_equalTo(<span class="hljs-number">50</span>).priorityHigh();
      make.height.mas_equalTo(<span class="hljs-number">50</span>).priority(<span class="hljs-number">200</span>);
      make.height.mas_equalTo(<span class="hljs-number">100</span>).priority(<span class="hljs-number">800</span>);
  &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-9">设置约束连词</h3>
<p><code>with</code>和<code>and</code>，放到表达式中，却可以作为连词让链式表达式更接近自然语言</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//什么也没有做，只是返回自己本身</span>
  - (MASConstraint *)<span class="hljs-keyword">with</span> &#123;
    <span class="hljs-keyword">return</span> self;
  &#125;
  
  - (MASConstraint *)and &#123;
    <span class="hljs-keyword">return</span> self;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：以下三句作用效果一致</p>
<pre><code class="hljs language-js copyable" lang="js"> make.width.width.height.equalTo(@<span class="hljs-number">100</span>);
 make.width.and.height.equalTo(@<span class="hljs-number">100</span>);
 make.width.height.equalTo(@<span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-10">Masonry注意</h3>
<ul>
<li>使用Masonry添加约束之前，需要在<code>addSubview</code>之后才能使用，否则会导致崩溃</li>
<li>在添加约束时常会出现一些错误，约束出现问题的原因一般就是两种：约束冲突和缺少约束。对于这两种问题，可以通过调试和log排查</li>
</ul>
<hr>
<h3 data-id="heading-11">常见布局屏幕适配的方式</h3>
<ul>
<li><a href="https://juejin.cn/post/6983179458559606797" target="_blank" title="https://juejin.cn/post/6983179458559606797">Autoresizing</a></li>
<li><a href="https://juejin.cn/post/6983861948664250382" target="_blank" title="https://juejin.cn/post/6983861948664250382">AutoLayou</a></li>
<li><a href="https://juejin.cn/post/6985332589431259143" target="_blank" title="https://juejin.cn/post/6985332589431259143">VFL</a></li>
<li><a href="https://juejin.cn/post/6986475724265766949" target="_blank" title="https://juejin.cn/post/6986475724265766949">Masonry</a></li>
<li><a href="https://juejin.cn/post/6979390190192164878" target="_blank" title="https://juejin.cn/post/6979390190192164878">SnapKit</a></li>
</ul></div>  
</div>
            