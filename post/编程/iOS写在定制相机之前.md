
---
title: iOS写在定制相机之前
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Thu, 18 Feb 2021 19:20:42 GMT
thumbnail: 
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><ul>
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
<pre><code class="copyable">+ (Class)layerClass {
    return [AVCaptureVideoPreviewLayer class];
}
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>为了实时场景，layer即AVCaptureVideoPreviewLayer 是需要设置一个session的</p>
<pre><code class="copyable">// 设置属性
@property (nonatomic, strong) AVCaptureSession *session;

// Getter & Setter
- (AVCaptureSession *)session {
    return [(AVCaptureVideoPreviewLayer *)self.layer session];
}

- (void)setSession:(AVCaptureSession *)session {
    [(AVCaptureVideoPreviewLayer *)self.layer setSession:session];
}

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>需要设置聚焦之类的，此时需要对view上触碰的点转换成摄像头的位置</p>
<pre><code class="copyable">-(CGPoint)captureDevicePointForPoint:(CGPoint)point{
    AVCaptureVideoPreviewLayer *layer = (AVCaptureVideoPreviewLayer *)self.layer;
    //将屏幕上点击的位置转化成摄像头的位置
    return [layer captureDevicePointOfInterestForPoint:point];
}
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>Game Over. Code不行，多敲敲。</p>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            