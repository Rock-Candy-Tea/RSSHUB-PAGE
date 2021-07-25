
---
title: 'iOS-屏幕适配（SnapKit）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=4828'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 17:20:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=4828'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第27天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank" title="https://juejin.cn/post/6967194882926444557">更文挑战</a></p>
<h3 data-id="heading-0">SnapKit简介</h3>
<ul>
<li><code>SnapKit</code>是一个优秀的第三方自适应布局库，它可以让iOS、OS X应用更简单地实现自动布局（Auto Layout）</li>
<li>下载链接 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSnapKit%2FSnapKit" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SnapKit/SnapKit" ref="nofollow noopener noreferrer">SnapKit</a></li>
</ul>
<hr>
<h3 data-id="heading-1">SnapKit配置</h3>
<ul>
<li>使用pods方式引入类库，<code>pod 'SnapKit'</code></li>
<li>引入头文件 <code>import SnapKit</code></li>
</ul>
<hr>
<h3 data-id="heading-2">SnapKit使用</h3>
<p><strong>示例：</strong></p>
<pre><code class="hljs language-js copyable" lang="js">testView.snp.makeConstraints &#123; (make) <span class="hljs-keyword">in</span>
    make.left.equalToSuperview().offset(<span class="hljs-number">50</span>)
    make.right.equalToSuperview().offset(-<span class="hljs-number">50</span>)
    make.top.equalToSuperview().offset(<span class="hljs-number">50</span>)
    make.bottom.equalToSuperview().offset(-<span class="hljs-number">50</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本格式：（<code>make . </code>指定其的一个属性<code>.</code>约束关系）</p>
<pre><code class="hljs language-js copyable" lang="js">make.attr.constrains
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>make</code>:可认为是要布局的view的代理
<code>constrains</code>:约束可能是多级的组合，比如<code>make.left.equalToSuperview().offset(50)</code>的两级组合，显示找到父<code>view</code>的左边位置，再向右（X轴）移动50点</p>
<h3 data-id="heading-3">给控件添加、更新约束、引用约束、停用、启用</h3>
<ul>
<li>
<p>添加新的约束</p>
<pre><code class="hljs language-js copyable" lang="js">testView.snp.makeConstraints &#123; (make) <span class="hljs-keyword">in</span>
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>删除控件以前所有约束，添加新约束</p>
<pre><code class="hljs language-js copyable" lang="js">testView.snp.remakeConstraints &#123; (make) <span class="hljs-keyword">in</span>
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>更新约束，写哪条更新哪条，其他约束不变</p>
<pre><code class="hljs language-js copyable" lang="js">testView.snp.updateConstraints &#123; (make) <span class="hljs-keyword">in</span>
 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>引用约束，声明一个局部变量或者类属性来引用要修改的约束</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> topConstraint: Constraint? = nil
  
override func <span class="hljs-function"><span class="hljs-title">viewDidLoad</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>.viewDidLoad()        

    <span class="hljs-keyword">let</span> testView = UIView()
    testView.backgroundColor = UIColor.red
    self.view.addSubview(testView)
      
    testView.snp.makeConstraints &#123; (make) <span class="hljs-keyword">in</span>
        self.topConstraint = make.left.equalToSuperview().offset(<span class="hljs-number">100</span>).constraint
        make.right.equalToSuperview().offset(-<span class="hljs-number">100</span>)
        make.top.equalToSuperview().offset(<span class="hljs-number">100</span>)
        make.bottom.equalToSuperview().offset(-<span class="hljs-number">100</span>)
     &#125;
&#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>停用</p>
<pre><code class="hljs language-js copyable" lang="js">self.topConstraint?.deactivate()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>启用</p>
<pre><code class="hljs language-js copyable" lang="js">self.topConstraint?.activate()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">设置约束关系</h3>





























<table><thead><tr><th align="center">约束关系</th><th align="center">说明</th></tr></thead><tbody><tr><td align="center"><code>equalTo()</code></td><td align="center">设置属性等于某个数值</td></tr><tr><td align="center"><code>greaterThanOrEqualTo()</code></td><td align="center">设置属性大于或等于某个数值</td></tr><tr><td align="center"><code>lessThanOrEqualTo()</code></td><td align="center">设置属性小于或等于某个数值</td></tr><tr><td align="center"><code>multipliedBy()</code></td><td align="center">设置属性乘以因子后的值</td></tr><tr><td align="center"><code>dividedBy()</code></td><td align="center">设置属性除以因子后的值</td></tr></tbody></table>
<h3 data-id="heading-5">设置控件布局属性</h3>

























<table><thead><tr><th align="center">布局属性</th><th align="center">说明</th></tr></thead><tbody><tr><td align="center">尺寸</td><td align="center"><code>width</code>、<code>height</code>、<code>size</code></td></tr><tr><td align="center">边距</td><td align="center"><code>left</code>、<code>top</code>、<code>right</code>、<code>bottom</code>、<code>leading</code>、<code>trailing</code></td></tr><tr><td align="center">中心点</td><td align="center"><code>center</code>、<code>centerX</code>、<code>centerY</code></td></tr><tr><td align="center">边界</td><td align="center"><code>edges</code></td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//iOS8之后Masonry新出了几个属性：</span>
<span class="hljs-comment">//距离边框的距离，等同于选中Storyboard的Constrain to margins后加约束public var leftMargin: SnapKit.ConstraintMakerExtendable &#123; get &#125;</span>
public <span class="hljs-keyword">var</span> rightMargin: SnapKit.ConstraintMakerExtendable &#123; get &#125;
public <span class="hljs-keyword">var</span> topMargin: SnapKit.ConstraintMakerExtendable &#123; get &#125;
public <span class="hljs-keyword">var</span> bottomMargin: SnapKit.ConstraintMakerExtendable &#123; get &#125;
public <span class="hljs-keyword">var</span> leadingMargin: SnapKit.ConstraintMakerExtendable &#123; get &#125;
public <span class="hljs-keyword">var</span> trailingMargin: SnapKit.ConstraintMakerExtendable &#123; get &#125;
public <span class="hljs-keyword">var</span> centerXWithinMargins: SnapKit.ConstraintMakerExtendable &#123; get &#125;
public <span class="hljs-keyword">var</span> centerYWithinMargins: SnapKit.ConstraintMakerExtendable &#123; get &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>leading</code>与<code>left</code>，<code>trailing</code>与<code>right</code> 在正常情况下是等价的，但是当一些布局是从右至左时(比如阿拉伯文) 则会对调</p>
<h3 data-id="heading-6">设置约束偏移</h3>




















<table><thead><tr><th align="center">方法</th><th align="center">参数</th><th align="center">说明</th></tr></thead><tbody><tr><td align="center"><code>offset(CGFloat offset)</code></td><td align="center"><code>CGFloat</code></td><td align="center">控件属性相对于参照物偏移多少</td></tr><tr><td align="center"><code>insets(MASEdgeInsets insets)</code></td><td align="center"><code>MASEdgeInsets</code></td><td align="center">控件四边相对于参照物偏移多少</td></tr></tbody></table>
<p><code>offset</code>示例</p>
<pre><code class="hljs language-js copyable" lang="js">testView.snp.makeConstraints &#123; (make) <span class="hljs-keyword">in</span>
      make.left.equalToSuperview().offset(<span class="hljs-number">20</span>)
      make.right.equalToSuperview().offset(-<span class="hljs-number">20</span>)
      make.top.equalToSuperview().offset(<span class="hljs-number">20</span>)
      make.bottom.equalToSuperview().offset(-<span class="hljs-number">20</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>insets</code>示例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//具体父控件四周都是20间距</span>
testView.snp.makeConstraints &#123; (make) <span class="hljs-keyword">in</span>
      make.edges.equalToSuperview().inset(UIEdgeInsets.init(top: <span class="hljs-number">20</span>, <span class="hljs-attr">left</span>: <span class="hljs-number">20</span>, <span class="hljs-attr">bottom</span>: <span class="hljs-number">20</span>, <span class="hljs-attr">right</span>: <span class="hljs-number">20</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">设置约束优先级</h3>
<ul>
<li>SnapKit为我们提供了三个默认的方法，<code>required</code>、<code>high</code>、<code>medium</code>、<code>low</code>，优先级最大数值是1000
<pre><code class="hljs language-js copyable" lang="js">public <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> required: ConstraintPriority &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-number">1000.0</span>
&#125;
public <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> high: ConstraintPriority &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-number">750.0</span>
&#125;
public <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> medium: ConstraintPriority &#123;
      #<span class="hljs-keyword">if</span> os(OSX)
          <span class="hljs-keyword">return</span> <span class="hljs-number">501.0</span>
      #<span class="hljs-keyword">else</span>
          <span class="hljs-keyword">return</span> <span class="hljs-number">500.0</span>
      #endif
 &#125;
public <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> low: ConstraintPriority &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-number">250.0</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>自己设置优先级的值，可以通过<code>priority()</code>方法来设置
<pre><code class="hljs language-js copyable" lang="js">testView.snp.makeConstraints &#123; (make) <span class="hljs-keyword">in</span>
    make.center.equalToSuperview()
    make.width.equ  alTo(<span class="hljs-number">100</span>).priority(ConstraintPriority.low)
    make.width.equalTo(<span class="hljs-number">100</span>).priority(ConstraintPriority.high)
   
    make.height.equalTo(<span class="hljs-number">100</span>).priority(<span class="hljs-number">200</span>)
    make.height.equalTo(<span class="hljs-number">50</span>).priority(<span class="hljs-number">800</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<hr>
<h3 data-id="heading-8">SnapKit 注意</h3>
<ul>
<li>使用SnapKit添加约束之前，需要在<code>addSubview</code>之后才能使用，否则会导致崩溃</li>
<li>在添加约束时常会出现一些错误，约束出现问题的原因一般就是两种：约束冲突和缺少约束。对于这两种问题，可以通过调试和log排查</li>
</ul>
<hr>
<h3 data-id="heading-9">常见布局屏幕适配的方式</h3>
<ul>
<li><a href="https://juejin.cn/post/6983179458559606797" target="_blank" title="https://juejin.cn/post/6983179458559606797">Autoresizing</a></li>
<li><a href="https://juejin.cn/post/6983861948664250382" target="_blank" title="https://juejin.cn/post/6983861948664250382">AutoLayou</a></li>
<li><a href="https://juejin.cn/post/6985332589431259143" target="_blank" title="https://juejin.cn/post/6985332589431259143">VFL</a></li>
<li><a href="https://juejin.cn/post/6986475724265766949" target="_blank" title="https://juejin.cn/post/6986475724265766949">Masonry</a></li>
<li><a href="https://juejin.cn/post/6979390190192164878" target="_blank" title="https://juejin.cn/post/6979390190192164878">SnapKit</a></li>
</ul></div>  
</div>
            