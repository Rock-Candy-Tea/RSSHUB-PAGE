
---
title: iOS写在定制相机之前
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Thu, 18 Feb 2021 19:20:42 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>
<p>问题</p>
<p>不是所有的拍照UIImagePickerController都能搞定，理由如下：</p>
<p>1.产品不整点幺蛾子，哪来体验创新</p>
<p>2.设计不整点幺蛾子，怎能体现用心</p>
<p>3.运营：这体验跟某宝某信咋不一样？？？</p>
<p>4.开发：我是被逼成大佬的！！！1.2.3.层层施压，大厂能搞得，你咋搞不了</p>
</li>
<li>
<p>思路：</p>
<p>定制相机，绕不开的问题：UIImagePickerController中那块实时场景怎么搞？</p>
<p>方案上一般是采用AVCaptureSession + AVCaptureVideoPreviewLayer</p>
<p>AVCaptureVideoPreviewLayer继承CALayer, 设置bounds、frame, 可满足简单需求</p>
<p>But, 横竖屏切换、iPhone与iPad共用、视图效果调整【毕竟上面的1.2.话语权普遍大过开发】等此类情况下，frame的方式哪有约束来的实在</p>
<p>每个view都有一个layer属性，定制view的layer为AVCaptureVideoPreviewLayer, view约束调整改变frame即可</p>
</li>
<li>
<p>上菜</p>
<ul>
<li>
<p>定义一个view</p>
<pre><code class="copyable">@interface AVPreView : UIView

@end
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>设置layerClass</p>
<pre><code class="copyable">+ (Class)layerClass &#123;
    return [AVCaptureVideoPreviewLayer class];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>为了实时场景，layer即AVCaptureVideoPreviewLayer 是需要设置一个session的</p>
<pre><code class="copyable">// 设置属性
@property (nonatomic, strong) AVCaptureSession *session;

// Getter & Setter
- (AVCaptureSession *)session &#123;
    return [(AVCaptureVideoPreviewLayer *)self.layer session];
&#125;

- (void)setSession:(AVCaptureSession *)session &#123;
    [(AVCaptureVideoPreviewLayer *)self.layer setSession:session];
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>需要设置聚焦之类的，此时需要对view上触碰的点转换成摄像头的位置</p>
<pre><code class="copyable">-(CGPoint)captureDevicePointForPoint:(CGPoint)point&#123;
    AVCaptureVideoPreviewLayer *layer = (AVCaptureVideoPreviewLayer *)self.layer;
    //将屏幕上点击的位置转化成摄像头的位置
    return [layer captureDevicePointOfInterestForPoint:point];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>Game Over. Code不行，多敲敲。</p>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            