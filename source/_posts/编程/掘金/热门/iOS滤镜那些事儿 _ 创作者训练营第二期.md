
---
title: 'iOS滤镜那些事儿 _ 创作者训练营第二期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d178ef34afe248a88955873b3acf97d4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 19:05:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d178ef34afe248a88955873b3acf97d4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一. <code>GPUImage</code> 框架的介绍及基本使用</h3>
<h4 data-id="heading-1">1.<code>GPUImage</code> 的介绍</h4>
<p>GPUImage是基于<code>OpenGL ES</code>的一套图像、视频处理开源框架，它里面提供了大量的滤镜，使用者可以通过这些滤镜的组合实现很好的效果，同时也很方便在原有基础上实现自定义的滤镜。对于大规模并行操作（如处理图像或实时视频帧），GPU具有比CPU更显着的性能优势。而 GPUImage 所有滤镜是基于<code>OpenGL Shader</code>实现的，所以滤镜效果、图像处理是在GPU上执行的，处理效率比较高，在iPhone4及其以上手机，可以做到实时流畅的效果。而且它隐藏了<code>Objective-C</code>与<code>OpenGL ES</code> API交互的复杂性。目前市面上的图像视频处理App，95%以上在使用GPUImage，所以学习它的使用及原理还是很有必要的。GPUImage 同时支持iOS跟Andorid平台，地址：<a href="https://github.com/BradLarson/GPUImage" target="_blank" rel="nofollow noopener noreferrer">iOS版本</a> <a href="https://github.com/cats-oss/android-gpuimage/blob/master/README.md" target="_blank" rel="nofollow noopener noreferrer">Android版本</a> 也支持 <a href="https://github.com/BradLarson/GPUImage2" target="_blank" rel="nofollow noopener noreferrer">Swift版本</a>，本文主要介绍它的 OC 版本，核心类的功能以及原理跟 Andorid 版本是相通的。
iOS开发者使用方式：直接 CocaPods 集成：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">pod 'GPUImage'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先来看下它的基本结构图：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d178ef34afe248a88955873b3acf97d4~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-04-11 下午3.56.11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从这张图中我们可以看到GPUImage的几个核心类:<code>GPUImageOutput</code> <code>GPUImageFilter</code> <code>GPUImageInput 协议</code> <code>GPUImageFrameBuffer</code>,接下来我们重点讲解这几个类。</p>
<h4 data-id="heading-2">2.核心功能类说明</h4>
<h5 data-id="heading-3"><code>GPUImageOutput</code></h5>
<p><code>GPUImageOutput</code> 是所有滤镜输入源的基类，也就是滤镜链的起点，先看下他的继承关系：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ae45f6181434f80946fa4bff13be058~tplv-k3u1fbpfcp-zoom-1.image" alt="GPUImageOutput" loading="lazy" referrerpolicy="no-referrer"><br>
分别解释一下这几种类型：<br></p>
<ul>
<li><code>GPUImagePicture</code></li>
</ul>
<p>通过图片来初始化，本质上是先将图片转化为 CGImageRef，然后将 CGImageRef 转化为纹理。<br></p>
<ul>
<li><code>GPUImageVideoCamera</code>:通过相机来初始化,本质是封装了AVCaptureVideoDataOutput来获取持续的视频流数据输出，在代理方法<code>captureOutput:didOutputSampleBuffer:fromConnection:</code>拿到 CMSampleBufferRef，将其转化为纹理的过程。<code>GPUImageStillCamera</code>是 GPUImageVideoCamera 的子类，可以用它来实现拍照功能。<br></li>
<li><code>GPUImageUIElement</code>:可以通过 UIView 或者 CALayer 来初始化。这个类可以用来实现在视频上添加文字水印的功能。<br></li>
<li><code>GPUImageTextureInput</code>:通过已经存在的纹理来初始化.<br></li>
<li><code>GPUImageRawDataInput</code>:通过二进制数据初始化，然后将二进制数据转化为纹理.<br></li>
<li><code>GPUImageMovie</code>:通过本地的视频来初始化。首先通过 AVAssetReader 来逐帧读取视频,然后将帧数据转化为纹理。</li>
<li><code>GPUImageFilter</code>:比较特殊，它既继承自 GPUImageOutput,又遵守协议 GPUImageInput 协议,所以它既可以作为滤镜链的源头，又可以把渲染的纹理输出给遵守 GPUImageInput 协议的类。是滤镜的核心，后面会单独介绍。<br></li>
</ul>
<h6 data-id="heading-4">核心功能与方法：</h6>
<p>想象一下，一个滤镜链的源头能做什么呢：</p>
<ol>
<li>需要产出一个渲染对象，这个需要渲染的对象就是<code>GPUImageFrameBuffer</code>.几个关于frameBuffer的方法：</li>
</ol>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (GPUImageFramebuffer *)framebufferForOutput;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法可以获得当前正在渲染的frameBuffer</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)removeOutputFramebuffer;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法用来移除当前渲染的frameBuffer</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)setInputFramebufferForTarget:(id<GPUImageInput>)target atIndex:(NSInteger)inputTextureIndex;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法的调用发生在当前output渲染完毕后，需要通知下一个receiver可以开始渲染的时候，把当前Output的FrameBuffer传递给下一个Input，让它可以使用这个FrameBuffer的结果进行渲染。</p>
<ol start="2">
<li>Target的添加以及管理，用来生成整个FilterChain.<br></li>
</ol>
<p>GPUImageOutput 既然作为一个滤镜的源头，相对应的就得有接受者接受它输出的 FrameBuffer ,这些接受者就是Target,而且有可能有多个接受者。管理这些target的主要方法：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)addTarget:(id<GPUImageInput>)newTarget;
- (void)addTarget:(id<GPUImageInput>)newTarget atTextureLocation:(NSInteger)textureLocation;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个addTarget方法的作用都是将下一个实现了GPUImageInput协议的对象添加到FilterChain当中来.一旦添加到滤镜链后，在当前Output渲染完成后就会收到通知，从而进行下一步的处理。</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (NSArray*)targets;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个Output都可以添加多个target,这个方法可以获取到当前Output所有的target.</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)removeTarget:(id<GPUImageInput>)targetToRemove;
- (void)removeAllTargets;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个方法的作用是将某一个或者所有的target都移出FilterChain。当一个target被移出FilterChain之后，它将不会再收到任何当前Output渲染完成的通知。</p>
<ol start="3">
<li>获取当前的GPUImageOutput对FrameBuffer的处理结果</li>
</ol>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (CGImageRef)newCGImageFromCurrentlyProcessedOutput;
- (CGImageRef)newCGImageByFilteringCGImage:(CGImageRef)imageToFilter;
- (UIImage *)imageFromCurrentFramebuffer;
- (UIImage *)imageFromCurrentFramebufferWithOrientation:(UIImageOrientation)imageOrientation;
- (UIImage *)imageByFilteringImage:(UIImage *)imageToFilter;
- (CGImageRef)newCGImageByFilteringImage:(UIImage *)imageToFilter;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中最核心的方法是<code>newCGImageFromCurrentlyProcessedOutput</code>，基本上所有的方法最终都调用了这个方法。但是GPUImageOutput并没有为这个方法提供默认的实现，而是提供了一个方法定义。具体的实现在它的两个重要的子类 GPUImageFilter 和 GPUImageFilterGroup 中。而实际上最终调用的方法都在 GPUImageFilter 中实现了.</p>
<h5 data-id="heading-5"><code>GPUImageInput</code>协议</h5>
<p><code>GPUImageInput</code> 是一个协议，它定义了一个能够接收 FrameBuffer 的 receiver 所必须实现的基本功能。实现这个协议的类可以作为渲染的终点使用。
实现了 GPUImageInput 接口的类：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8df2eb78a4d44a89118af1e9eca0e9f~tplv-k3u1fbpfcp-zoom-1.image" alt="GPUImageInput协议" loading="lazy" referrerpolicy="no-referrer">
对这几个类进行解释：<br></p>
<ul>
<li><code>GPUImageMovieWriter</code>：封装了 AVAssetWriter，可以逐帧从帧缓存的渲染结果中读取数据，最后通过 AVAssetWriter 将视频文件保存到指定的路径。<br></li>
<li><code>GPUImageView</code>：继承自 UIView，通过输入的纹理，执行一遍渲染流程。我们一般使用它来呈现渲染结果。<br></li>
<li><code>GPUImageTextureOutput</code>：它可以获取到输入的Framebuffer中的纹理对象.<br></li>
<li><code>GPUImageRawDataOutput</code>：通过 rawBytesForImage 属性，可以获取到当前输入纹理的二进制数据。</li>
</ul>
<h6 data-id="heading-6">核心功能与方法：</h6>
<p>可以作为滤镜链的终点。基本功能主要包括：</p>
<ul>
<li>接收 GPUmageOutput 的输出信息;</li>
<li>接收上一个GPUImageOutput渲染完成的通知,并且完成自己的处理;</li>
</ul>
<ol>
<li>接收GPUmageOutput的输出信息对应方法：</li>
</ol>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)setInputFramebuffer:(GPUImageFramebuffer *)newInputFramebuffer atIndex:(NSInteger)textureIndex;
- (NSInteger)nextAvailableTextureIndex;
- (void)setInputSize:(CGSize)newSize atIndex:(NSInteger)textureIndex;
- (void)setInputRotation:(GPUImageRotationMode)newInputRotation atIndex:(NSInteger)textureIndex;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据这些方法可以看到，GPUImageInput 可以接收的信息包括上一个Output输出的FrameBuffer，FrameBuffer的size以及rotation。这些 textureIndex 都是为了提供个需要多个input的Filter准备的。
2. 接收GPUImageOutput渲染完成的通知对应方法：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)newFrameReadyAtTime:(CMTime)frameTime atIndex:(NSInteger)textureIndex;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上一个 GPUImageOutput 渲染完成后会通知它所有的 Target，可以参考下它在<code>GPUImageFilter</code>里面的实现。</p>
<h5 data-id="heading-7"><code>GPUImageFrameBuffer</code></h5>
<p>GPUImageFrameBuffer 提供了在 GPUImageOutput 和 GPUImageInput 进行数据传递的媒介。在整个渲染流程中，GPUImageFrameBuffer作为一个纽带，将各个不同的元素串联起来；每个GPUImageFrameBuffer 都有一个自己的OpenGL Texture，每个 GPUImageOutput 都会输出一个 GPUImageFrameBuffer 对象，而每个 GPUImageInput都实现了一个<code>setInputFramebuffer:atIndex:</code>方法，来接收上一个Output处理完的纹理.</p>
<ul>
<li>GPUImageFrameBuffer 的获取逻辑，是由<code>GPUImageFrameBufferCache</code> 进行管理的，需要时从BufferCache中获取，使用完成后，被BufferCache回收。FrameBuffer 的创建跟存储是需要消耗资源的，所以 GPUImage 为了尽量减少资源的消耗，会将使用完成的 FrameBuffer 存储在缓存中，每次通过 输入的纹理size 跟 TextureOptions 作为 key 从hash map 中获取。</li>
</ul>
<h5 data-id="heading-8"><code>GPUImageFilter</code></h5>
<p>GPUImageFilter 是整个GPUImage框架的核心,GPUImage所内置的100多种滤镜效果都继承于此类。例如我们经常用到的一些滤镜：</p>
<ul>
<li><code>GPUImageBrightnessFilter</code>:亮度调整滤镜</li>
<li><code>GPUImageExposureFilter</code>:曝光调整滤镜</li>
<li><code>GPUImageContrastFilter</code>:对比度调整滤镜</li>
<li><code>GPUImageSaturationFilter</code>:饱和度调整滤镜</li>
<li><code>GPUImageWhiteBalanceFilter</code>:白平衡调整滤镜</li>
<li><code>GPUImageColorInvertFilter</code>:反转图像的颜色</li>
<li><code>GPUImageCropFilter</code>:将图像裁剪到特定区域</li>
<li><code>GPUImageGaussianBlurFilter</code>:可变半径高斯模糊</li>
<li><code>GPUImageSketchFilter</code>:素描滤镜</li>
<li><code>GPUImageToonFilter</code>:卡通效果</li>
<li><code>GPUImageDissolveBlendFilter</code>:两个图像的混合</li>
<li><code>GPUImageFilterPipeline</code> : 链式组合滤镜</li>
</ul>
<p>...</p>
<h6 data-id="heading-9">核心功能与方法：</h6>
<ol>
<li>
<p>GPUImageFilter是GPUImageOutput的子类，但是同时它也实现了GPUImageInput协议。因此，它包含了一个Input和Output的所有功能。既它可以接受一个待渲染对象，渲染完成后继续传递给下一个实现GPUImageInput协议的接受者。具体的方法调用我们在下一小节的 滤镜底层源码分析中讲解。</p>
</li>
<li>
<p>提供根据不同的顶点着色器(VertexShader)与片元着色器(FragmentShader)来初始化渲染程序(GLProgram)的方法，但是整个渲染过程是一样的，因此这个过程都被封装到了基类中；</p>
</li>
</ol>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (id)initWithVertexShaderFromString:(NSString *)vertexShaderString fragmentShaderFromString:(NSString *)fragmentShaderString;
- (id)initWithFragmentShaderFromString:(NSString *)fragmentShaderString;
- (id)initWithFragmentShaderFromFile:(NSString *)fragmentShaderFilename;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里简单介绍一下这几个<code>OPenGL</code>的术语</p>
<ul>
<li><code>VertexShader</code>:顶点着色器，<code>OPenGL</code> 接收用户传递的几何数据（顶点信息和几何图元），这些数据经过顶点着色器后可以确定图形的形状以及位置。顶点着色器是 OPenGL 渲染过程的第一个着色器。</li>
<li>光栅化：是将图形的立体位置转换成在屏幕上显示的像素片元的过程；</li>
<li><code>FragmentShader</code>:对光栅化的像素点进行着色就要使用片元着色器。它是<code>OPenGL</code>渲染过程的最后一个着色器。</li>
<li><code>GLProgram</code>: <code>OpenGL ES</code>的program的面向对象封装,包括了VertexShader，FragmentShader的加载，program的link以及对attribute和uniform的获取和管理.</li>
</ul>
<p>这里主要是一些根据不同的着色器进行创建Program的方法。</p>
<ol start="3">
<li>作为基类提供给子类可以进行覆盖的方法。</li>
</ol>
<blockquote>
<p>用一句话来总结GPUImageFilter的作用：就是用来接收源图像(FrameBuffer)，通过自定义的顶点、片元着色器来渲染新的图像，并在绘制完成后通知响应链的下一个对象。</p>
</blockquote>
<h4 data-id="heading-10">3.GPUImage滤镜的使用</h4>
<p>我们先来看它的应用效果<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40b35716cb81473caac0da9f2304e57d~tplv-k3u1fbpfcp-zoom-1.image" alt="效果" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e88a62b686394f2bb48fa8625a66f531~tplv-k3u1fbpfcp-zoom-1.image" alt="效果2" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-11">(1) 为图片添加滤镜</h5>
<p>直接上代码：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">   /**初始化滤镜源头*/
    GPUImagePicture *imagePic = [[GPUImagePicture alloc] initWithImage:[UIImage imageNamed:@"picOne.jpg"]];
    /**创建滤镜*/
    GPUImageGaussianBlurFilter *gaussianBlur = [[GPUImageGaussianBlurFilter alloc] init];
    gaussianBlur.blurRadiusInPixels = 10;
    /**添加接受者，即target*/
    [imagePic addTarget:gaussianBlur];
    /**增加frameBUffer 计数防止被移除*/
    [gaussianBlur useNextFrameForImageCapture];
    /**开始处理图片*/
    [imagePic processImage];
    /**根据frameBuffer 获取图片*/
    self.showImageView.image = [gaussianBlur imageFromCurrentFramebuffer];
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-12">流程说明：</h6>
<ul>
<li>使用图片初始化滤镜源头<code>GPUImagePicture</code></li>
<li>初始化滤镜效果<code>GPUImageGaussianBlurFilter</code></li>
<li>为当前滤镜源添加接收者Target <code>addTarget</code></li>
<li><code>useNextFrameForImageCapture</code>:方法是防止帧缓存被移除，如果不调用这个方法会导致Framebuffer被移除，从而导致Crash</li>
<li>根据滤镜的渲染结果FrameBuffer导出图片<code>[gaussianBlur imageFromCurrentFramebuffer]</code></li>
</ul>
<h5 data-id="heading-13">(2) 摄像头捕获视频流添加滤镜</h5>
<p>核心代码：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)setupCamera
&#123;
    //videoCamera
    self.gpuVideoCamera = [[GPUImageVideoCamera alloc] initWithSessionPreset:AVCaptureSessionPreset640x480 cameraPosition:AVCaptureDevicePositionBack];
    self.gpuVideoCamera.outputImageOrientation = [[UIApplication sharedApplication] statusBarOrientation];
    //GPUImageView填充模式
    self.gpuImageView.fillMode = kGPUImageFillModePreserveAspectRatioAndFill;
    //空白效果
    GPUImageFilter *clearFilter = [[GPUImageFilter alloc] init];
    [self.gpuVideoCamera addTarget:clearFilter];
    [clearFilter addTarget:self.gpuImageView];
    //Start camera capturing, 里面封装的是AVFoundation的session的startRunning
    [self.gpuVideoCamera startCameraCapture];
&#125;
#pragma mark - Action && Notification
- (IBAction)originalBtnDown:(id)sender &#123;
    /**先移除target*/
    [self.gpuVideoCamera removeAllTargets];
    //空白效果
    GPUImageFilter *clearFilter = [[GPUImageFilter alloc] init];
    [self.gpuVideoCamera addTarget:clearFilter];
    [clearFilter addTarget:self.gpuImageView];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">(3) 混合滤镜的使用</h5>
<p>核心代码：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">    GPUImageView *filterView = [[GPUImageView alloc] initWithFrame:self.view.frame];
    filterView.center = self.view.center;
    filterView.fillMode = kGPUImageFillModePreserveAspectRatioAndFill;
    [self.view addSubview:filterView];
    /*初始化混合滤镜*/
    filter = [[GPUImageDissolveBlendFilter alloc] init];
    /*设置滤镜混合度*/
    [(GPUImageDissolveBlendFilter *)filter setMix:0.5];
    /*初始化视频输出源*/
    NSURL *sampleURL = [[NSBundle mainBundle] URLForResource:@"IMG_4278" withExtension:@"MOV"];
    movieFile = [[GPUImageMovie alloc] initWithURL:sampleURL];
    movieFile.runBenchmark = YES;
    movieFile.playAtActualSpeed = YES;
    /*初始化摄像头输出源*/
    videoCamera = [[GPUImageVideoCamera alloc] initWithSessionPreset:AVCaptureSessionPreset640x480 cameraPosition:AVCaptureDevicePositionBack];
    videoCamera.outputImageOrientation = UIInterfaceOrientationPortrait;
    NSString *pathToMovie = [NSHomeDirectory() stringByAppendingPathComponent:@"Documents/Movie.m4v"];
    unlink([pathToMovie UTF8String]);
    NSURL *movieURL = [NSURL fileURLWithPath:pathToMovie];
    //初始化接受者
    movieWriter = [[GPUImageMovieWriter alloc] initWithMovieURL:movieURL size:CGSizeMake(480.0, 640.0)];
    GPUImageFilter* progressFilter = [[GPUImageFilter alloc] init];
    [movieFile addTarget:progressFilter];
    //设置输出方向
    [progressFilter setInputRotation:kGPUImageRotateRight atIndex:0];
    // 响应链
    [progressFilter addTarget:filter];
    [videoCamera addTarget:filter];
    //设置音源
     movieWriter.shouldPassthroughAudio = YES;
     movieFile.audioEncodingTarget = movieWriter;
     [movieFile enableSynchronizedEncodingUsingMovieWriter:movieWriter];
     // 显示到界面
    [filter addTarget:filterView];
    //添加到接收者
    [filter addTarget:movieWriter];
    [videoCamera startCameraCapture];
    [movieWriter startRecording];
    [movieFile startProcessing];
      /*写入结束后保存视频*/
    __weak typeof(self) weakSelf = self;
    [movieWriter setCompletionBlock:^&#123;
        __strong typeof(self) strongSelf = weakSelf;
        [strongSelf->filter removeTarget:strongSelf->movieWriter];
        [strongSelf->movieWriter finishRecording];
         /*根据movieURL保存视频到本地*/
         // ...
     &#125;];

<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-15">流程说明：</h6>
<ul>
<li>混合滤的核心是<code>GPUImageDissolveBlendFilter</code>的使用，它继承自<code>GPUImageTwoInputFilter</code>,它需要有两个输入源</li>
<li>初始化两个输入源<code>GPUImageVideoCamera</code>跟<code>GPUImageMovie</code></li>
<li>添加输入源到DissolveBlendFilter</li>
<li>添加filter到输出数据源<code>GPUImageMovieWriter</code></li>
</ul>
<h5 data-id="heading-16">(4) 为视频添加水印</h5>
<p>核心代码：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">    GPUImageView *filterView = [[GPUImageView alloc] initWithFrame:self.view.frame];
    self.view = filterView;
    // 混合滤镜初始化
    filter = [[GPUImageDissolveBlendFilter alloc] init];
    //混合度
    [(GPUImageDissolveBlendFilter *)filter setMix:0.5];
    // 本地视频播放源
    NSURL *sampleURL = [[NSBundle mainBundle] URLForResource:@"IMG_4278" withExtension:@"MOV"];
    AVAsset *asset = [AVAsset assetWithURL:sampleURL];
    CGSize size = self.view.bounds.size;
    //设置moive源头
    movieFile = [[GPUImageMovie alloc] initWithAsset:asset];
    movieFile.runBenchmark = YES;
    movieFile.playAtActualSpeed = YES;
    // 水印
    UILabel *label = [[UILabel alloc] initWithFrame:CGRectMake(100, 100, 100, 100)];
    label.text = @"我是水印";
    label.font = [UIFont systemFontOfSize:30];
    label.textColor = [UIColor redColor];
    [label sizeToFit];
    UIImage *image = [UIImage imageNamed:@"watermark.png"];
    UIImageView *imageView = [[UIImageView alloc] initWithImage:image];
    UIView *subView = [[UIView alloc] initWithFrame:CGRectMake(0, 0, size.width, size.height)];
    subView.backgroundColor = [UIColor clearColor];
    imageView.center = CGPointMake(subView.bounds.size.width / 2, subView.bounds.size.height / 2);
    [subView addSubview:imageView];
    [subView addSubview:label];
    //设置UI源头
    GPUImageUIElement *uielement = [[GPUImageUIElement alloc] initWithView:subView];
    //GPUImageTransformFilter 动画的filter
    NSString *pathToMovie = [NSHomeDirectory() stringByAppendingPathComponent:@"Documents/Movie.m4v"];
    unlink([pathToMovie UTF8String]);
    NSURL *movieURL = [NSURL fileURLWithPath:pathToMovie];
    //初始化接受者
    movieWriter = [[GPUImageMovieWriter alloc] initWithMovieURL:movieURL size:CGSizeMake(480.0, 640.0)];
    //为调整视频方向添加一个空白滤镜
    GPUImageFilter* progressFilter = [[GPUImageFilter alloc] init];
    [movieFile addTarget:progressFilter];
    //设置方向
    [progressFilter setInputRotation:kGPUImageRotateRight atIndex:0];

    [progressFilter addTarget:filter];
    [uielement addTarget:filter];
    movieWriter.shouldPassthroughAudio = YES;
    movieFile.audioEncodingTarget = movieWriter;
    [movieFile enableSynchronizedEncodingUsingMovieWriter:movieWriter];
     // 显示到界面
    [filter addTarget:filterView];
    [filter addTarget:movieWriter];
    //开始记录
    [movieWriter startRecording];
    [movieFile startProcessing];
    __weak typeof(self) weakSelf = self;
    //每一帧处理完成 大约30帧/秒
    [progressFilter setFrameProcessingCompletionBlock:^(GPUImageOutput *output, CMTime time)&#123;
        CGRect frame = imageView.frame;
        frame.origin.x += 1;
        frame.origin.y += 1;
        imageView.frame = frame;
        //更新UIElement
        [uielement updateWithTimestamp:time];
    &#125;];
    [movieWriter setCompletionBlock:^&#123;
        __strong typeof(self) strongSelf = weakSelf;
        [strongSelf->filter removeTarget:strongSelf->movieWriter];
        [strongSelf->movieWriter finishRecording];
          /*根据movieURL保存视频到本地*/
         // ... 
    &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-17">流程说明：</h6>
<ul>
<li>混合滤镜的核心是<code>GPUImageDissolveBlendFilter</code>的使用，它继承自<code>GPUImageTwoInputFilter</code>,它需要有两个输入源</li>
<li>初始化两个输入源<code>GPUImageVideoCamera</code>跟<code>GPUImageUIElement</code></li>
<li>其他同上</li>
</ul>
<h5 data-id="heading-18">(5) 滤镜组的使用</h5>
<p>核心代码</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">    //创建摄像头视图
    GPUImageView *filterView = [[GPUImageView alloc]initWithFrame:self.view.bounds];
    //显示模式充满整个边框
    filterView.fillMode = kGPUImageFillModePreserveAspectRatioAndFill;
    [self.view addSubview:filterView];
    //初始化滤镜源
    self.stillCamera = [[GPUImageStillCamera alloc]initWithSessionPreset:AVCaptureSessionPresetPhoto cameraPosition:AVCaptureDevicePositionBack];
    //输出图像旋转方式
    self.stillCamera.outputImageOrientation = UIInterfaceOrientationPortrait;
    //反色滤镜
    GPUImageColorInvertFilter *filter1 = [[GPUImageColorInvertFilter alloc]init];
    //浮雕滤镜
    GPUImageEmbossFilter *filter2 = [[GPUImageEmbossFilter alloc]init];
    //GPUImageToonFilter *filter3 = [[GPUImageToonFilter alloc] init];
    GPUImageFilterGroup *groupFilter = [[GPUImageFilterGroup alloc]init];
    [groupFilter addFilter:filter1];
    [groupFilter addFilter:filter2];
    //[groupFilter addFilter:filter3];
    [filter1 addTarget:filter2];
    //[filter2 addTarget:filter3];
    //定义了一个变量来保存filter-chain上的最后一个filter,后面保存图片时调用的方法里要用到。
    self.lastFilter = filter2;
    //设置第一个滤镜
    groupFilter.initialFilters = @[filter1];
    //设置最后一个滤镜
    groupFilter.terminalFilter = filter2;
    [self.stillCamera addTarget:groupFilter];
    [groupFilter addTarget:filterView];
    //解决第一帧黑屏,音频缓冲区是在视频缓冲区之前写入的。
    [self.stillCamera addAudioInputsAndOutputs];
    [self.view bringSubviewToFront:self.catchBtn];
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(0.1 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^&#123;
        //开始捕捉
        [self.stillCamera startCameraCapture];
    &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-19">流程说明：</h6>
<ul>
<li>混合滤的核心是<code>GPUImageFilterGroup</code>的使用</li>
<li>初始化多个滤镜并且添加到滤镜组</li>
<li>设置Group的第一个以及最后一个滤镜</li>
<li>输出</li>
</ul>
<h3 data-id="heading-20">二. <code>GPUImage</code> 底层源码分析</h3>
<h4 data-id="heading-21">1.滤镜链加载流程分析</h4>
<p>通过上面的Demo例子我们能够分析滤镜链的使用流程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc00c0287ba147c49a708ceb5982c01b~tplv-k3u1fbpfcp-zoom-1.image" alt="GPUImageFilter流" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们以图片添加滤镜的例子分析GPUImage的滤镜方法调用流程：</p>
<ul>
<li>使用图片初始化滤镜源头<code>GPUImagePicture</code>,调用方法：</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (id)initWithImage:(UIImage *)newImageSource;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法里面又会调用</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">outputFramebuffer = [[GPUImageContext sharedFramebufferCache] fetchFramebufferForSize:pixelSizeToUseForTexture onlyTexture:YES];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法最主要的作用是根据图片的大小去<code>GPUImageFramebufferCache</code>中去获取一块 FrameBuffer,也就是<code>outputFramebuffer</code></p>
<ul>
<li>滤镜的初始化，根据当前自己的顶点着色器以及片元着色器初始化滤镜，以及创建OPenGL ES的渲染程序 <code>GLProgram</code></li>
<li>为滤镜源添加Target：<code>- (void)addTarget:(id<GPUImageInput>)newTarget;</code>. 在这个方法里面会调用</li>
</ul>
<p><code>[self setInputFramebufferForTarget:newTarget atIndex:textureLocation];</code>
最终会调用<code>[target setInputFramebuffer:[self framebufferForOutput] atIndex:inputTextureIndex];</code>方法.这个方法最主要的作用是把当前Output的输出 Framebuffer 传递给接受者.</p>
<ul>
<li><code>- (void)useNextFrameForImageCapture;</code>设置成员变量<code>usingNextFrameForImageCapture = YES</code>代表着输出的结果会被用于获取图像,所以在渲染的核心方法</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (void)renderToTextureWithVertices:(const GLfloat *)vertices textureCoordinates:(const GLfloat *)textureCoordinates;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对<code>outputFramebuffer</code>加锁，因为默认情况下，当下一个input渲染完成之后，就会释放这个 FrameBuffer。如果你需要对当前的Filter的输出进行截图的话，则需要保留住这个 FrameBuffer。</p>
<ul>
<li>接下来调用方法<code>[imagePic processImage];</code>: 开始进入滤镜处理流程，接着调用方法<code>-(BOOL)processImageWithCompletionHandler:(void (^)(void))completion;</code>在这个方法内部调用了Target的两个方法，进行OutputFrameBuffer的渲染与向下传递.</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> [currentTarget setInputFramebuffer:outputFramebuffer atIndex:textureIndexOfTarget];
 [currentTarget newFrameReadyAtTime:kCMTimeIndefinite atIndex:textureIndexOfTarget];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个方法的作用是获取从上个Output传递过来的 Framebuffer，并进行加锁操作。<br>
第二个方法的作用是利用自身<code>GLProgram</code>进行渲染，并且调用<code>- (void)informTargetsAboutNewFrameAtTime:(CMTime)frameTime;</code>把渲染结果向下一个实现<code>GPUImageInput</code>协议的滤镜传递。</p>
<ul>
<li><code>[gaussianBlur imageFromCurrentFramebuffer];</code> 方法：根据 Framebuffer 获取图片，里面调用<code>- (CGImageRef)newCGImageFromCurrentlyProcessedOutput</code> 方法，完成图片获取以及释放GCD信号量。</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">if (dispatch_semaphore_wait(imageCaptureSemaphore, convertedTimeout) != 0)
  &#123;
        return NULL;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里信号量的作用是等待渲染完成。完成后走下面的获取图片流程。整个的方法调用流程可以参考下面的图片：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a971ae6db94c4abc920e9d50d2004c87~tplv-k3u1fbpfcp-zoom-1.image" alt="方法调用栈" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">2.滤镜渲染流程分析</h4>
<p>渲染是整个<code>GPUImageFilter</code> 的核心，在初始化方法中完成了<code>OpenGL ES Program</code>的创建好并且link成功了之后，我们就可以使用这个Program进行渲染了。整个渲染的过程发生在<code>- (void)renderToTextureWithVertices:textureCoordinates:</code>中。我们也借着解析这个方法来了解一下<code>OpenGL ES</code>的渲染过程：</p>
<ul>
<li><code>[GPUImageContext setActiveShaderProgram:filterProgram];</code>: 将初始化后得到Progrm 上下文设置为默认的context，并且激活。调用的<code>GPUImageContext</code>方法</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">+ (void)setActiveShaderProgram:(GLProgram *)shaderProgram;
&#123;
    GPUImageContext *sharedContext = [GPUImageContext sharedImageProcessingContext];
    [sharedContext setContextShaderProgram:shaderProgram];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>获取一个待渲染的<code>GPUImageFrameBuffer</code>,这个FrameBuffer 会根据输入纹理的尺寸(inputTextureSize)以及纹理信息(outputTextureOptions) 去<code>GPUImageFrameBufferCahe</code>中获取。大致流程为：存在符合要求的Framebuffer就返回一个，没有就去创建。</li>
<li>根据<code>usingNextFrameForImageCapture</code>判断当前Framebuffer是否用于获取图片，如果是则进行加锁。</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c"> if (usingNextFrameForImageCapture)
    &#123; //将这个outputFrameBuffer进行lock。
        [outputFramebuffer lock];
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将整个FrameBuffer的数据使用backgroundColor进行清空：</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl">glClearColor(backgroundColorRed, backgroundColorGreen, backgroundColorBlue, backgroundColorAlpha);
glClear(GL_COLOR_BUFFER_BIT);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将上一个Output传递过来的FrameBuffer作为texture用来渲染：</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl">glActiveTexture(GL_TEXTURE2);
glBindTexture(GL_TEXTURE_2D, [firstInputFramebuffer <span class="hljs-built_in">texture</span>]);
glUniform1i(filterInputTextureUniform, <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>将顶点的位置信息以及顶点的纹理坐标信息作为attribute传递给GPU：</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl">glVertexAttribPointer(filterPositionAttribute, <span class="hljs-number">2</span>, GL_FLOAT, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-keyword">vertices</span>);
glVertexAttribPointer(filterTextureCoordinateAttribute, <span class="hljs-number">2</span>, GL_FLOAT, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, textureCoordinates);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>进行渲染：</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl">glDrawArrays(GL_TRIANGLE_STRIP, <span class="hljs-number">0</span>, <span class="hljs-number">4</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>最后将上一个<code>GPUImageOutput</code>传递过来的FrameBuffer使命已经完成，对其进行解锁释放：</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">[firstInputFramebuffer unlock];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整个渲染过程完成。</p>
<h3 data-id="heading-23">三. 自定义滤镜</h3>
<h4 data-id="heading-24">1.如何加载一个自定义滤镜</h4>
<p>通过上面的学习我们知道，滤镜的效果实际是根据不同的顶点着色器以及片元着色器来实现的。自定义滤镜实际就是自定义这两种着色器。有两种方式来加载我们的自定义滤镜</p>
<ul>
<li>自定义滤镜类，继承自<code>GPUImageFilter</code>,然后用字符串常量形式加载我们的Shader代码例如：</li>
</ul>
<pre><code class="hljs language-glsl copyable" lang="glsl">NSString *<span class="hljs-keyword">const</span> kGPUImageBrightnessFragmentShaderString = SHADER_STRING
(
 <span class="hljs-keyword">varying</span> <span class="hljs-keyword">highp</span> <span class="hljs-type">vec2</span> textureCoordinate;
 <span class="hljs-keyword">uniform</span> <span class="hljs-type">sampler2D</span> inputImageTexture;
 <span class="hljs-keyword">uniform</span> <span class="hljs-keyword">lowp</span> <span class="hljs-type">float</span> brightness;
 
 <span class="hljs-type">void</span> main()
 &#123;
     <span class="hljs-keyword">lowp</span> <span class="hljs-type">vec4</span> textureColor = <span class="hljs-built_in">texture2D</span>(inputImageTexture, textureCoordinate);
     <span class="hljs-built_in">gl_FragColor</span> = <span class="hljs-type">vec4</span>((textureColor.rgb + <span class="hljs-type">vec3</span>(brightness)), textureColor.w);
 &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后根据<code>GPUImageFilter</code>提供的初始化方法进行加载。</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (id)initWithVertexShaderFromString:(NSString *)vertexShaderString fragmentShaderFromString:(NSString *)fragmentShaderString;
- (id)initWithFragmentShaderFromString:(NSString *)fragmentShaderString;
- (id)initWithFragmentShaderFromFile:(NSString *)fragmentShaderFilename;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>另一种方式:如果只是自定义<code>FragmentShader</code>，可以是将Shader语句封装为fsh结尾的文件，然后调用下面方法进行加载</li>
</ul>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">- (id)initWithFragmentShaderFromFile:(NSString *)fragmentShaderFilename;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">2. 一些特殊的自定义滤镜效果</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b6c0e265b754541930d7c83b151de00~tplv-k3u1fbpfcp-zoom-1.image" alt="自定义滤镜" loading="lazy" referrerpolicy="no-referrer"><br>
一些特殊的滤镜效果,比如抖音的滤镜效果（闪白、灵魂出窍、抖动、缩放、毛刺、眩晕等）可以查看我的<a href="https://github.com/chenXming/GPUIamage_demo.git" target="_blank" rel="nofollow noopener noreferrer">GitHub</a>.
关于自定义滤镜部分需要你对<code>OPenGL ES</code>、线性代数以及算法有基础的了解，并且熟悉<code>GLSL着色语言</code>,如果想进一步学习可以参考GLSL的官方快速入门指导<a href="https://www.khronos.org/opengles/sdk/docs/reference_cards/OpenGL-ES-2_0-Reference-card.pdf" target="_blank" rel="nofollow noopener noreferrer">OpenGL ES</a>,我们这篇文章不在涉及。</p>
<h3 data-id="heading-26">四. 总结</h3>
<p>这篇文章主要是介绍了<code>GPUImage</code>的使用、滤镜链加载流程、渲染逻辑，还有一些模块未涉及到，比如<code>GLProgram</code>的创建、link过程,<code>GPUImageMovieComposition</code>视频编辑模块，滤镜的自定义流程等，需要感兴趣的同学自己探究。</p>
<h4 data-id="heading-27">1.进一步学习需要掌握的内容</h4>
<p><a href="http://www.amazon.com/OpenGL-Shading-Language-Randi-Rost/dp/0321637631/ref=sr_1_1?s=books&ie=UTF8&qid=1422896457&sr=1-1&keywords=opengl+shading+language" target="_blank" rel="nofollow noopener noreferrer">The OpenGL Shading Language</a><br>
<a href="http://www.shaderific.com/glsl-functions" target="_blank" rel="nofollow noopener noreferrer">GLSL内建的函数介绍</a></p>
<h4 data-id="heading-28">2.一些参考引用</h4>
<p><a href="https://github.com/BradLarson/GPUImage" target="_blank" rel="nofollow noopener noreferrer">github.com/BradLarson/…</a><br>
<a href="https://www.khronos.org/opengles/sdk/docs/reference_cards/OpenGL-ES-2_0-Reference-card.pdf" target="_blank" rel="nofollow noopener noreferrer">www.khronos.org/opengles/sd…</a><br>
<a href="https://www.jianshu.com/u/8367278ff6cf" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/u/8367278ff…</a><br></p></div>  
</div>
            