
---
title: '学习CoreAnimation - 隐式动画篇'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85674b4e7d0240ba8390d0125bad5c90~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:46:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85674b4e7d0240ba8390d0125bad5c90~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>隐式动画</strong>：改变CALyer图层属性，通过CoreAnimation来控制所执行的动画</p>
<h3 data-id="heading-0">系统如何实现隐式动画</h3>
<p>1、当CALyer的属性被修改的时候，会调用actionForyKey方法，来传递属性名称</p>
<p>2、通过搜索属性名称，会返回nil或者CAAction协议对应的对象，CALyer通过返回的结果，去和当前或先前的值做动画，这里由CoreAnimation来完成，nil值无动画，非空值对应动画的属性内容</p>
<h3 data-id="heading-1">事务</h3>
<p>动画并不需要手动打开，相反需要明确的关闭，否则会一直存在。我们在处理动画过程中会遇到，我们并不需要指定明确的动画类型，仅仅通过改变一个属性，让coreAnimation来决定最适合的动画。</p>
<p><code>事务决定动画的实际执行时间，图层行为决定动画类型。</code>事务通过CATransaction类做管理，并且只能用begin（入栈）、commit（出栈）处理，不可以被初始化创建。</p>
<p>每一个可以用来做动画的图层属性，都会被添加到栈顶的事务，任何一次runloop循环都会将改变的属性集中起来，并以0.25s（默认事务动画时间）的频率执行。当我们设置AnimationDuration，可以控制事务的动画时间，使它变快或者变慢。</p>
<p>如果我们直接修改动画当前事务的时间，会导致同一时间如果有别的动画也会受到影响，因此我们只需要在调整或改变动画时间之前，压入一个新的事务</p>
<pre><code class="copyable">CATransaction.begin()
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在属性改变后</p>
<pre><code class="copyable">CATransaction.commit()
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>UIView中beginAnimations和commitAnimations动画，也是基于内部实现了CATransaction，但是在最新的API中明确表示在iOS13后弃用这两个隐式调用的方法，而更加推荐我们使用animatewithDuration的block方法，在block函数中所有属性的改变都会被事务包含，进而避免了误操作begin和commit的风险。</p>
<h3 data-id="heading-2">事务的回调</h3>
<p>CATransaction为我们提供了一个回调，也就是说如果我们使用这个完成回调方法，当我们规定的动画完成后会调，你可以在这个代码块内部执行下一步动画的操作。</p>
<pre><code class="copyable">setCompletionBlock &#123;&#125;
// 生命周期：在上一次事务提交并出栈以后才会执行，执行时没有新的事务，所以使用系统默认的事务（系统默认事务时间0.25s）
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">图层行为（重点）</h3>
<p>上面说的一切内容都是基于CALyer下图层的属性改变，而不是UIView中所关联的layer图层，在代码调试的过程中，我尝试使用UIView的layer图层进行属性改变的动画操作，发现在这一过程中，我所期待的隐式动画特性并没有发挥作用</p>
<p><strong>--UIView做了什么？</strong></p>
<p>每个UIView对它关联的图层都扮演了一个委托，并且提供了一个actionForLayer:forKey:实现方法，当UIVIew不在block动画的代码块中执行动画，UIView默认会对图层的行为返回nil，如果执行在block动画块的内部，就返回一个非空值</p>
<p>可以打印一下这段代码</p>
<pre><code class="copyable">let outside = fivrView.action(for: fivrView.layer, forKey: "backgroundColor")
print("Outside: \(outside.debugDescription)")

UIView.animate(withDuration: 1) &#123;
    let inside = self.fivrView.action(for: self.fivrView.layer, forKey: "backgroundColor")
    print("Inside: \(inside.debugDescription)")
&#125;
        
//or
UIView.beginAnimations(nil, context: nil)
        
let inside = self.fivrView.action(for: self.fivrView.layer, forKey: "backgroundColor")
print("Inside: \(inside.debugDescription)")
        
UIView.commitAnimations()
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，当属性在动画块之外发生改变，UIview通过返回nil来禁止隐式动画，同时这个特性被UIView关闭，当然还可以调用以下代码，控制是否禁用隐式动画</p>
<pre><code class="copyable">CATransaction.setDisableActions(Bool)
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>--总结</strong></p>
<ul>
<li><code>UIView</code>关联的图层禁用了隐式动画，对这种图层做动画的唯一办法就是使用<code>UIView</code>的动画函数（而不是依赖<code>CATransaction</code>），或者继承<code>UIView</code>，并覆盖<code>-actionForLayer:forKey:</code>方法，或者直接创建一个显式动画（具体细节见《iOS核心动画高级技巧》第八章）。</li>
<li>对于单独存在的图层，我们可以通过实现图层的<code>-actionForLayer:forKey:</code>委托方法，或者提供一个<code>actions</code>字典来控制隐式动画。</li>
</ul>
<p><strong>--行为</strong></p>
<p><strong>行为</strong>通常是一个被Core Animation<em>隐式</em>调用的<em>显式</em>动画对象。<strong>自定义行为</strong>就是我们将显示的动画作为CALyer的属性添加。这里我们使用是<code>actions</code>字典可以写更少的代码。</p>
<h3 data-id="heading-4">图层的动态呈现（重点理解）</h3>
<p>当我们设置CALyer的属性，实际上只是定义图层动画<strong>结束后的变化</strong>，而不是直接通过更新图层的属性值去改变它的内容，理解这段话主要在于理解，这层机制中<strong>变化</strong>二字的含义。<code>图层需要在变化中产生动画，而非将属性直接作用图层。</code></p>
<p>当设置<code>CALayer</code>的属性，实际上是在定义当前事务结束之后图层如何显示的<em>模型</em>。Core Animation扮演了一个<em>控制器</em>的角色，并且负责根据图层行为和事务设置去不断更新<em>视图</em>的这些属性在屏幕上的状态。</p>
<p>如果动画时间超过了屏幕刷新时间，coreAnimation需要对屏幕上的图层进行重新组织，并被记录屏幕上每个图层属性的显示值，又被叫做呈现图层。呈现图层是一个独立的图层，可以通过presentationLayer获取呈现图层，<code>呈现图层实际上是模型图层的复制，但它的属性值代表了在任何指定时刻当前外观效果，可以通过获取它的值来获取屏幕上真正显示的值。</code></p>
<p>呈现图层会在图层首次提交的时候被创建（在屏幕上第一次显示的时候）多数情况下，我们不需要直接去访问呈现图层。</p>
<p><strong>·引用官方图片·</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85674b4e7d0240ba8390d0125bad5c90~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="7.4.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>·引用官方的代码·</strong></p>
<p>##使用<strong>hitTest</strong>可以用来判断指定图层是否被触摸</p>
<pre><code class="copyable">colorLayer.frame = CGRect(x: 0, y: 0, width: 100, height: 100)
        
colorLayer.position = CGPoint(x: self.view.bounds.size.width / 2, y: self.view.bounds.size.height / 2)
        
colorLayer.backgroundColor = UIColor.red.cgColor
        
view.layer.addSublayer(colorLayer)

override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) &#123;
        for touch in touches &#123;
            let point = touch.location(in: self.view)
            if ((self.colorLayer.presentation()?.hitTest(point)) != nil) &#123;
                let red = arc4random() / UInt32(INT_MAX)
                let green = arc4random() / UInt32(INT_MAX)
                let blue = arc4random() / UInt32(INT_MAX)
                
                self.colorLayer.backgroundColor = UIColor(red: CGFloat(red), green: CGFloat(green), blue: CGFloat(blue), alpha: 1).cgColor
            &#125;else &#123;
                CATransaction.begin()
                
                CATransaction.setAnimationDuration(4)
                
                self.colorLayer.position = point
                
                CATransaction.commit()
            &#125;
            
        &#125;
    &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>--归纳</strong></p>
<p>基于上面内容我们可以得出比较<code>清晰的结论</code>：</p>
<blockquote>
<p>呈现图层的属性值特性适合处理同步动画和手势跟随</p>
<p>使用presentationLayer可以获取它，当我们获取它的时候其实是对原模型图层的拷贝</p>
<p>以呈现图层为参考放在交互层面对于用户而言是精准的</p>
<p>它和模型图层的关系：呈现取决于动画轨迹，模型取决于动画起终点</p>
</blockquote>
<h3 data-id="heading-5">∗∗∗最后∗∗∗</h3>
<p><strong>这一章节理论居多，总结为四个点：1.事务对动画的影响2.隐式动画的成因3.图层的行为4.图层的动态值呈现。在学习的过程中的推敲和探索也能发现趣味性，明白原生API最初的设计思路，对于理解CoreAnimation非常有意义。</strong></p></div>  
</div>
            