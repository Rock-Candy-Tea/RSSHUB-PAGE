
---
title: 'iOS事件处理，看我就够了~'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4fbb4346a81489bacfe141e06d4a03c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 23:45:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4fbb4346a81489bacfe141e06d4a03c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4fbb4346a81489bacfe141e06d4a03c~tplv-k3u1fbpfcp-zoom-1.image" alt="博客配图" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">UIResponder</h3>
<p>**<code>UIResponder</code>是iOS中用于处理用户事件的API，可以处理触摸事件、按压事件<code>(3D touch)</code>、远程控制事件、硬件运动事件。**可以通过<code>touchesBegan</code>、<code>pressesBegan</code>、<code>motionBegan</code>、<code>remoteControlReceivedWithEvent</code>等方法，获取到对应的回调消息。<code>UIResponder</code>不只用来接收事件，还可以处理和传递对应的事件，如果当前响应者不能处理，则转发给其他合适的响应者处理。</p>
<p>应用程序通过响应者来接收和处理事件，响应者可以是继承自<code>UIResponder</code>的任何子类，例如<code>UIView</code>、<code>UIViewController</code>、<code>UIApplication</code>等。当事件来到时，系统会将事件传递给合适的响应者，并且将其成为第一响应者。</p>
<p>第一响应者未处理的事件，将会在响应者链中进行传递，传递规则由<code>UIResponder</code>的<code>nextResponder</code>决定，可以通过重写该属性来决定传递规则。当一个事件到来时，第一响应者没有接收消息，则顺着响应者链向后传递。</p>
<h3 data-id="heading-1">查找第一响应者</h3>
<h4 data-id="heading-2">基础API</h4>
<p>查找第一响应者时，有两个非常关键的<code>API</code>，查找第一响应者就是通过不断调用子视图的这两个<code>API</code>完成的。</p>
<p>调用方法，获取到被点击的视图，也就是第一响应者。</p>
<pre><code class="hljs language-objc copyable" lang="objc">- (<span class="hljs-built_in">UIView</span> *)hitTest:(<span class="hljs-built_in">CGPoint</span>)point withEvent:(<span class="hljs-built_in">UIEvent</span> *)event;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>hitTest:withEvent:</code>方法内部会通过调用这个方法，来判断点击区域是否在视图上，是则返回<code>YES</code>，不是则返回<code>NO</code>。</p>
<pre><code class="hljs language-objc copyable" lang="objc">- (<span class="hljs-built_in">BOOL</span>)pointInside:(<span class="hljs-built_in">CGPoint</span>)point withEvent:(<span class="hljs-built_in">UIEvent</span> *)event;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">查找第一响应者</h4>
<p><strong>应用程序接收到事件后，将事件交给<code>keyWindow</code>并转发给根视图，根视图按照视图层级逐级遍历子视图，并且遍历的过程中不断判断视图范围，并最终找到第一响应者。</strong></p>
<p>从<code>keyWindow</code>开始，向前逐级遍历子视图，不断调用<code>UIView</code>的<code>hitTest:withEvent:</code>方法，通过该方法查找在点击区域中的视图后，并继续调用返回视图的子视图的<code>hitTest:withEvent:</code>方法，以此类推。如果子视图不在点击区域或没有子视图，则当前视图就是第一响应者。</p>
<p>在<code>hitTest:withEvent:</code>方法中，会从上到下遍历子视图，并调用<code>subViews</code>的<code>pointInside:withEvent:</code>方法，来找到点击区域内且最上面的子视图。如果找到子视图则调用其<code>hitTest:withEvent:</code>方法，并继续执行这个流程，以此类推。如果子视图不在点击区域内，则忽略这个视图及其子视图，继续遍历其他视图。</p>
<p>可以通过重写对应的方法，控制这个遍历过程。通过重写<code>pointInside:withEvent:</code>方法，来做自己的判断并返回<code>YES</code>或<code>NO</code>，返回点击区域是否在视图上。通过重写<code>hitTest:withEvent:</code>方法，返回被点击的视图。</p>
<p>此方法在遍历视图时，忽略以下三种情况的视图，如果视图具有以下特征则忽略。但是视图的背景颜色是<code>clearColor</code>，并不在忽略范围内。</p>
<ol>
<li>视图的<code>hidden</code>等于YES。</li>
<li>视图的<code>alpha</code>小于等于0.01。</li>
<li>视图的<code>userInteractionEnabled</code>为NO。</li>
</ol>
<p>如果点击事件是发生在视图外，但在其子视图内部，子视图也不能接收事件并成为第一响应者。这是因为在其父视图进行<code>hitTest:withEvent:</code>的过程中，就会将其忽略掉。</p>
<h3 data-id="heading-4">事件传递</h3>
<h4 data-id="heading-5">传递过程</h4>
<ol>
<li><code>UIApplication</code>接收到事件，将事件传递给<code>keyWindow</code>。</li>
<li><code>keyWindow</code>遍历<code>subViews</code>的<code>hitTest:withEvent:</code>方法，找到点击区域内合适的视图来处理事件。</li>
<li><code>UIView</code>的子视图也会遍历其<code>subViews</code>的<code>hitTest:withEvent:</code>方法，以此类推。</li>
<li>直到找到点击区域内，且处于最上方的视图，将视图逐步返回给<code>UIApplication</code>。</li>
<li>在查找第一响应者的过程中，已经形成了一个响应者链。</li>
<li>应用程序会先调用第一响应者处理事件。</li>
<li>如果第一响应者不能处理事件，则调用其<code>nextResponder</code>方法，一直找响应者链中能处理该事件的对象。</li>
<li>最后到<code>UIApplication</code>后仍然没有能处理该事件的对象，则该事件被废弃。</li>
</ol>
<p>模拟代码</p>
<pre><code class="hljs language-objc copyable" lang="objc">- (<span class="hljs-built_in">UIView</span> *)hitTest:(<span class="hljs-built_in">CGPoint</span>)point withEvent:(<span class="hljs-built_in">UIEvent</span> *)event &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">self</span>.alpha <= <span class="hljs-number">0.01</span> || <span class="hljs-keyword">self</span>.userInteractionEnabled == <span class="hljs-literal">NO</span> || <span class="hljs-keyword">self</span>.hidden) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">nil</span>;
    &#125;
    
    <span class="hljs-built_in">BOOL</span> inside = [<span class="hljs-keyword">self</span> pointInside:point withEvent:event];
    <span class="hljs-keyword">if</span> (inside) &#123;
        <span class="hljs-built_in">NSArray</span> *subViews = <span class="hljs-keyword">self</span>.subviews;
        <span class="hljs-comment">// 对子视图从上向下找</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-built_in">NSInteger</span> i = subViews.count - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
            <span class="hljs-built_in">UIView</span> *subView = subViews[i];
            <span class="hljs-built_in">CGPoint</span> insidePoint = [<span class="hljs-keyword">self</span> convertPoint:point toView:subView];
            <span class="hljs-built_in">UIView</span> *hitView = [subView hitTest:insidePoint withEvent:event];
            <span class="hljs-keyword">if</span> (hitView) &#123;
                <span class="hljs-keyword">return</span> hitView;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">self</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">nil</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">示例</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ab91fa8bb354c2d9829da920208a145~tplv-k3u1fbpfcp-zoom-1.image" alt="事件传递示例" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，响应者链如下：</p>
<ol>
<li>如果点击<code>UITextField</code>后其会成为第一响应者。</li>
<li>如果<code>textField</code>未处理事件，则会将事件传递给下一级响应者链，也就是其父视图。</li>
<li>父视图未处理事件则继续向下传递，也就是<code>UIViewController</code>的<code>View</code>。</li>
<li>如果控制器的<code>View</code>未处理事件，则会交给控制器处理。</li>
<li>控制器未处理则会交给<code>UIWindow</code>。</li>
<li>然后会交给<code>UIApplication</code>。</li>
<li>最后交给<code>UIApplicationDelegate</code>，如果其未处理则丢弃事件。</li>
</ol>
<p>事件通过<code>UITouch</code>进行传递，在事件到来时，第一响应者会分配对应的<code>UITouch</code>，<code>UITouch</code>会一直跟随着第一响应者，并且根据当前事件的变化<code>UITouch</code>也会变化，当事件结束后则<code>UITouch</code>被释放。</p>
<p><code>UIViewController</code>没有<code>hitTest:withEvent:</code>方法，所以控制器不参与查找响应视图的过程。但是控制器在响应者链中，如果控制器的<code>View</code>不处理事件，会交给控制器来处理。控制器不处理的话，再交给<code>View</code>的下一级响应者处理。</p>
<h4 data-id="heading-7">注意</h4>
<ol>
<li>在执行<code>hitTest:withEvent:</code>方法时，如果该视图是<code>hidden</code>等于NO的那三种被忽略的情况，则改视图返回<code>nil</code>。</li>
<li>如果当前视图在响应者链中，但其没有处理事件，则不考虑其兄弟视图，即使其兄弟视图和其都在点击范围内。</li>
<li><code>UIImageView</code>的<code>userInteractionEnabled</code>默认为NO，如果想要<code>UIImageView</code>响应交互事件，将属性设置为YES即可响应事件。</li>
</ol>
<h3 data-id="heading-8">事件控制</h3>
<h4 data-id="heading-9">事件拦截</h4>
<p>有时候想让指定视图来响应事件，不再向其子视图继续传递事件，可以通过重写<code>hitTest:withEvent:</code>方法。在执行到方法后，直接将该视图返回，而不再继续遍历子视图，这样响应者链的终端就是当前视图。</p>
<pre><code class="copyable">- (UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event &#123;
    return self;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">事件转发</h4>
<p>在开发过程中，经常会遇到子视图显示范围超出父视图的情况，这时候可以重写该视图的<code>pointInside:withEvent:</code>方法，将点击区域扩大到能够覆盖所有子视图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67bd196441c04d018de0cea8d5a4375b~tplv-k3u1fbpfcp-zoom-1.image" alt="扩大响应区域" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设有上面的视图结构，<code>SuperView</code>的<code>Subview</code>超出了其视图范围，如果点击<code>Subview</code>在父视图外面的部分，则不能响应事件。所以通过重写<code>pointInside:withEvent:</code>方法，将响应区域扩大为虚线区域，包含<code>SuperView</code>的所有子视图，即可让子视图响应事件。</p>
<h4 data-id="heading-11">事件逐级传递</h4>
<p>如果想让响应者链中，每一级<code>UIResponder</code>都可以响应事件，可以在每级<code>UIResponder</code>中都实现<code>touches</code>并调用<code>super</code>方法，即可实现响应者链事件逐级传递。</p>
<p>只不过这并不包含<code>UIControl</code>子类以及<code>UIGestureRecognizer</code>的子类，这两类会直接打断响应者链。</p>
<h3 data-id="heading-12">Gesture Recognizer</h3>
<p><strong>如果有事件到来时，视图有附加的手势识别器，则手势识别器优先处理事件。如果手势识别器没有处理事件，则将事件交给视图处理，视图如果未处理则顺着响应者链继续向后传递。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ea6dc994d2a4ceba06403bd32318fb5~tplv-k3u1fbpfcp-zoom-1.image" alt="手势识别" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当响应者链和手势同时出现时，也就是既实现了<code>touches</code>方法又添加了手势，会发现<code>touches</code>方法有时会失效，这是因为手势的执行优先级是高于响应者链的。</p>
<p>事件到来后先会执行<code>hitTest</code>和<code>pointInside</code>操作，通过这两个方法找到第一响应者，这个在上面已经详细讲过了。当找到第一响应者并将其返回给<code>UIApplication</code>后，<code>UIApplication</code>会向第一响应者派发事件，并且遍历整个响应者链。如果响应者链中能够处理当前事件的手势，则将事件交给手势处理，并调用<code>touches</code>的<code>cancelled</code>方法将响应者链取消。</p>
<p>在<code>UIApplication</code>向第一响应者派发事件，并且遍历响应者链查找手势时，会开始执行响应者链中的<code>touches</code>系列方法。会先执行<code>touchesBegan</code>和<code>touchesMoved</code>方法，如果响应者链能够继续响应事件，则执行<code>touchesEnded</code>方法表示事件完成，如果将事件交给手势处理则调用<code>touchesCancelled</code>方法将响应者链打断。</p>
<p>根据苹果的官方文档，手势不参与响应者链传递事件，但是也通过<code>hitTest</code>的方式查找响应的视图，手势和响应者链一样都需要通过<code>hitTest</code>方法来确定响应者链的。在<code>UIApplication</code>向响应者链派发消息时，只要响应者链中存在能够处理事件的手势，则手势响应事件，如果手势不在响应者链中则不能处理事件。</p>
<p><a href="https://developer.apple.com/documentation/uikit/uigesturerecognizer" target="_blank" rel="nofollow noopener noreferrer">Apple UIGestureRecognizer Documentation</a></p>
<h3 data-id="heading-13">UIControl</h3>
<p>根据上面的手势和响应者链的处理规则，我们会发现<code>UIButton</code>或者<code>UISlider</code>等控件，并不符合这个处理规则。<code>UIButton</code>可以在其父视图已经添加<code>tapGestureRecognizer</code>的情况下，依然正常响应事件，并且<code>tap</code>手势不响应。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0b8bbde5d3d46f486173aa3b93673c1~tplv-k3u1fbpfcp-zoom-1.image" alt="UIControl" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以<code>UIButton</code>为例，<code>UIButton</code>也是通过<code>hitTest</code>的方式查找第一响应者的。区别在于，如果<code>UIButton</code>是第一响应者，则直接由<code>UIApplication</code>派发事件，不通过<code>Responder Chain</code>派发。如果其不能处理事件，则交给手势处理或响应者链传递。</p>
<p>不只<code>UIButton</code>是直接由<code>UIApplication</code>派发事件的，所有继承自<code>UIControl</code>的类，都是由<code>UIApplication</code>直接派发事件的。</p>
<p><a href="https://developer.apple.com/documentation/uikit/uicontrol" target="_blank" rel="nofollow noopener noreferrer">Apple UIControl Documentation</a></p>
<h3 data-id="heading-14">事件传递优先级</h3>
<h4 data-id="heading-15">测试</h4>
<p>为了有依据的推断响应事件的实现和传递机制，我们做以下测试。</p>
<h6 data-id="heading-16">示例1</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/780ba0dbc24e46b5bea5dca3c7624643~tplv-k3u1fbpfcp-zoom-1.image" alt="示例1" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设<code>RootView</code>、<code>SuperView</code>、<code>Button</code>都实现<code>touches</code>方法，并且<code>Button</code>添加<code>buttonAction:</code>的<code>action</code>，点击<code>button</code>后的调用如下。</p>
<pre><code class="hljs language-objc copyable" lang="objc">RootView -> hitTest:withEvent:
RootView -> pointInside:withEvent:
SuperView -> hitTest:withEvent:
SuperView -> pointInside:withEvent:
Button -> hitTest:withEvent:
Button -> pointInside:withEvent:
RootView -> hitTest:withEvent:
RootView -> pointInside:withEvent:

Button -> touchesBegan:withEvent:
Button -> touchesEnded:withEvent:
Button -> buttonAction:
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-17">示例2</h6>
<p>还是上面的视图结构，我们给<code>RootView</code>加上<code>UITapGestureRecognizer</code>手势，并且通过<code>tapAction:</code>方法接收回调，点击上面的<code>SuperView</code>后，方法调用如下。</p>
<pre><code class="hljs language-objc copyable" lang="objc">RootView -> hitTest:withEvent:
RootView -> pointInside:withEvent:
SuperView -> hitTest:withEvent:
SuperView -> pointInside:withEvent:
Button -> hitTest:withEvent:
Button -> pointInside:withEvent:
RootView -> hitTest:withEvent:
RootView -> pointInside:withEvent:

RootView -> gestureRecognizer:shouldReceivePress:
RootView -> gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:
SuperView -> touchesBegan:withEvent:
RootView -> gestureRecognizerShouldBegin:
RootView -> tapAction:
SuperView -> touchesCancelled:
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-18">示例3</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/230647a708ca47a0a8c98d66dd0a1cea~tplv-k3u1fbpfcp-zoom-1.image" alt="示例3" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的视图中<code>Subview1</code>、<code>Subview2</code>、<code>Subview3</code>是同级视图，都是<code>SuperView</code>的子视图。我们给<code>Subview1</code>加上<code>UITapGestureRecognizer</code>手势，并且通过<code>subView1Action:</code>方法接收回调，点击上面的<code>Subview3</code>后，方法调用如下。</p>
<pre><code class="hljs language-objc copyable" lang="objc">SuperView -> hitTest:withEvent:
SuperView -> pointInside:withEvent:
Subview3 -> hitTest:withEvent:
Subview3 -> pointInside:withEvent:
SuperView -> hitTest:withEvent:
SuperView -> pointInside:withEvent:

Subview3 -> touchesBegan:withEvent:
Subview3 -> touchesEnded:withEvent:
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的例子来看，虽然<code>Subview1</code>在<code>Subview3</code>的下面，并且添加了手势，点击区域是在<code>Subview1</code>和<code>Subview3</code>两个视图上的。但是由于经过<code>hitTest</code>和<code>pointInside</code>之后，响应者链中并没有<code>Subview1</code>，所以<code>Subview1</code>的手势并没有被响应。</p>
<h4 data-id="heading-19">分析</h4>
<p><strong>根据我们上面的测试，推断iOS响应事件的优先级，以及整体的响应逻辑。</strong></p>
<p>当事件到来时，会通过<code>hitTest</code>和<code>pointInside</code>两个方法，从<code>Window</code>开始向上面的视图查找，找到第一响应者的视图。找到第一响应者后，系统会判断其是继承自<code>UIControl</code>还是<code>UIResponder</code>，如果是继承自<code>UIControl</code>，则直接通过<code>UIApplication</code>直接向其派发消息，并且不再向响应者链派发消息。</p>
<p>如果是继承自<code>UIResponder</code>的类，则调用第一响应者的<code>touchesBegin</code>，并且不会立即执行<code>touchesEnded</code>，而是调用之后顺着响应者链向后查找。如果在查找过程中，发现响应者链中有的视图添加了手势，则进入手势的代理方法中，如果代理方法返回可以响应这个事件，则将第一响应者的事件取消，并调用其<code>touchesCanceled</code>方法，然后由手势来响应事件。</p>
<p>如果手势不能处理事件，则交给第一响应者来处理。如果第一响应者也不能响应事件，则顺着响应者链继续向后查找，直到找到能够处理事件的<code>UIResponder</code>对象。如果找到<code>UIApplication</code>还没有对象响应事件的话，则将这次事件丢弃。</p>
<h3 data-id="heading-20">接收事件深度剖析</h3>
<p><strong>在<code>UIApplication</code>接收到响应事件之前，还有更复杂的系统级的处理，处理流程大致如下。</strong></p>
<ol>
<li>系统通过<code>IOKit.framework</code>来处理硬件操作，其中屏幕处理也通过<code>IOKit</code>完成(<code>IOKit</code>可能是注册监听了屏幕输出的端口)</li>
</ol>
<p>当用户操作屏幕，<code>IOKit</code>收到屏幕操作，会将这次操作封装为<code>IOHIDEvent</code>对象。通过<code>mach port</code>(IPC进程间通信)将事件转发给<code>SpringBoard</code>来处理。</p>
<ol start="2">
<li><code>SpringBoard</code>是iOS系统的桌面程序。<code>SpringBoard</code>收到<code>mach port</code>发过来的事件，唤醒<code>main runloop</code>来处理。</li>
</ol>
<p><code>main runloop</code>将事件交给<code>source1</code>处理，<code>source1</code>会调用<code>__IOHIDEventSystemClientQueueCallback()</code>函数。</p>
<ol start="3">
<li>函数内部会判断，是否有程序在前台显示，如果有则通过<code>mach port</code>将<code>IOHIDEvent</code>事件转发给这个程序。</li>
</ol>
<p>如果前台没有程序在显示，则表明<code>SpringBoard</code>的桌面程序在前台显示，也就是用户在桌面进行了操作。
<code>__IOHIDEventSystemClientQueueCallback()</code>函数会将事件交给<code>source0</code>处理，<code>source0</code>会调用<code>__UIApplicationHandleEventQueue()</code>函数，函数内部会做具体的处理操作。</p>
<ol start="4">
<li>例如用户点击了某个应用程序的icon，会将这个程序启动。</li>
</ol>
<p>应用程序接收到<code>SpringBoard</code>传来的消息，会唤醒<code>main runloop</code>并将这个消息交给<code>source1</code>处理，<code>source1</code>调用<code>__IOHIDEventSystemClientQueueCallback()</code>函数，在函数内部会将事件交给<code>source0</code>处理，并调用<code>source0</code>的<code>__UIApplicationHandleEventQueue()</code>函数。
在<code>__UIApplicationHandleEventQueue()</code>函数中，会将传递过来的<code>IOHIDEvent</code>转换为<code>UIEvent</code>对象。</p>
<ol start="5">
<li>在函数内部，调用<code>UIApplication</code>的<code>sendEvent:</code>方法，将<code>UIEvent</code>传递给第一响应者或<code>UIControl</code>对象处理，在<code>UIEvent</code>内部包含若干个<code>UITouch</code>对象。</li>
</ol>
<h6 data-id="heading-21">Tips</h6>
<p><code>source1</code>是<code>runloop</code>用来处理<code>mach port</code>传来的系统事件的，<code>source0</code>是用来处理用户事件的。
<code>source1</code>收到系统事件后，都会调用<code>source0</code>的函数，所以最终这些事件都是由<code>source0</code>处理的。</p>
<h3 data-id="heading-22">小技巧</h3>
<p>在开发中，有时会有找到当前<code>View</code>对应的控制器的需求，这时候就可以利用我们上面所学，根据响应者链来找到最近的控制器。</p>
<p>在<code>UIResponder</code>中提供了<code>nextResponder</code>方法，通过这个方法可以找到当前响应环节的上一级响应对象。可以从当前<code>UIView</code>开始不断调用<code>nextResponder</code>，查找上一级响应者链的对象，就可以找到离自己最近的<code>UIViewController</code>。</p>
<p>示例代码：</p>
<pre><code class="hljs language-objc copyable" lang="objc">- (<span class="hljs-built_in">UIViewController</span> *)parentController &#123;
   <span class="hljs-built_in">UIResponder</span> *responder = [<span class="hljs-keyword">self</span> nextResponder];
   <span class="hljs-keyword">while</span> (responder) &#123;
       <span class="hljs-keyword">if</span> ([responder isKindOfClass:[<span class="hljs-built_in">UIViewController</span> <span class="hljs-keyword">class</span>]]) &#123;
           <span class="hljs-keyword">return</span> (<span class="hljs-built_in">UIViewController</span> *)responder;
       &#125;
       responder = [responder nextResponder];
   &#125;
   <span class="hljs-keyword">return</span> <span class="hljs-literal">nil</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            