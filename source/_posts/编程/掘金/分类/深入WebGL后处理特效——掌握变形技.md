
---
title: '深入WebGL后处理特效——掌握变形技'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/158b9d60fde04c49a1bbbaaf948430c9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 22 May 2021 01:07:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/158b9d60fde04c49a1bbbaaf948430c9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><em>后处理(Post-processing)，是针对原有的游戏画面进行算法加工，达到提升画面质量或增强画面效果的技术，可通过着色器Shader程序实现。</em></p>
<h2 data-id="heading-0">概述</h2>
<p>变形特效是处理和增强画面效果的一类后处理技术，经常被应用在各类相机短视频app特效中，如美颜瘦身、哈哈镜特效。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/158b9d60fde04c49a1bbbaaf948430c9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>美颜相机的变形特效</em></p>
<p>本文主要从各类美颜相机中梳理了以下几种常用的变形特效：</p>
<ul>
<li>
<p>局部扭曲 (twirl effect)</p>
</li>
<li>
<p>局部膨胀 (inflate effect)</p>
</li>
<li>
<p>任意方向挤压 (pinch effect)</p>
</li>
</ul>
<p>其中，扭曲可用在眼睛的局部旋转，膨胀可以用于大眼，挤压/拉伸可用于脸部塑性和瘦脸等。如何通过着色器Shader实现这些变形，是本文讨论的重点。（ps:着急预览代码的童鞋见文末）</p>
<h2 data-id="heading-1">变形技原理</h2>
<p>虽然变形的效果千奇百怪，但它们往往离不开这三个要素：变形位置、影响范围和变形程度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47b77f7168ca44f89af2eeb797477cbf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>变形Shader实现人物尬舞</em></p>
<p>因此它在Shader中的实现，就是通过构造一个变形函数，将传入原始uv坐标，变形的位置、范围range和程度strength，经过计算后生成变形后的采样坐标，代码如下：</p>
<pre><code class="copyable">#iChannel0 "src/assets/texture/joker.png"

vec2 deform(vec2 uv, vec2 center, float range, float strength) &#123;
  // TODO: 变形处理
  return uv;
&#125;

void mainImage(out vec4 fragColor, vec2 coord) &#123;
    vec2 uv = coord / iResolution.xy;
    vec2 mouse = iMouse.xy / iResolution.xy;
    uv = deform(uv, mouse, .5, .5);
    vec3 color = texture(iChannel0, uv).rgb;
    fragColor.rgb = color;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>本文着色器代码采用GLSL规范，遵循Shader-Toy的写法，方便大家预览。</p>
</blockquote>
<h2 data-id="heading-2">变形小技巧：采样距离场变换</h2>
<p>我们设置定点坐标O，任意点到点O距离为dist，以不同dist值为半径，以点O为中心可形成无数个等距的采样圈，它们被称为点O的距离场。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bda0acf623b4b328f90c657b07bd583~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>采样距离场</em></p>
<p>我们可以通过改变采样圈的大小、位置，进而改变纹理采样位置，以实现膨胀/收缩、挤压的变形效果。</p>
<pre><code class="copyable">vec2 deform(vec2 uv, vec2 center, float range, float strength) &#123;
  float dist = distance(uv, center);
  vec2 direction = normalize(uv - center);
  dist = transform(dist, range, strength); // 改变采样圈半径
  center = transform(center, dist, range, strength); // 改变采样圈中心位置
  return center + dist * direction;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个技巧的应用先不急着说，现在我们还是从简单的扭曲变形开始讲。</p>
<h2 data-id="heading-3">扭曲</h2>
<p>扭曲效果类似旋涡形态，特点是越靠近中心点旋转程度越剧烈，我们可通过递减函数来表示离中心点距离d和对应旋转角度θ之间的关系。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f8c747f6bda49d78ffe5b7c3c7ec1ec~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如下图，采用简单的一次函数θ = -A/R *d + A，其中A表示扭曲中心的旋转角度，A为正数则表示旋转方向为顺时针，负数表示逆时针，R表示扭曲的边界；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65c8430f687246098e6afbd9184ba249~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>扭曲变形原理</em></p>
<p>如上图，扭曲函数入参A(中心旋转角Angle)和R(变形范围Range)可以这么描述： 1）A代表中心旋转角度，绝对值越大，扭曲程度更高； 2）A > 0表示扭曲方向为顺时针，反之A<0表示逆时针； 3）R代表扭曲边界，值越大，影响范围越大。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d31f2b6efb44838b790ca4aed36ece0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>扭曲动态效果</em></p>
<p>我们可以引入时间变量time动态改变A的值，产生扭动特效，如上图小丑扭跨效果，具体shader代码如下：</p>
<pre><code class="copyable">#iChannel0 "src/assets/texture/joker.png"
#define Range .3
#define Angle .5
#define SPEED 3.
mat2 rotate(float a) // 旋转矩阵
&#123;
    float s = sin(a);
    float c = cos(a);
    return mat2(c,-s,s,c);
&#125;
vec2 twirl(vec2 uv, vec2 center, float range, float angle) &#123;
    float d = distance(uv, center);
    uv -=center;
    // d = clamp(-angle/range * d + angle,0.,angle); // 线性方程
    d = smoothstep(0., range, range-d) * angle;
    uv *= rotate(d);
    uv+=center;
    return uv;
&#125;
void mainImage(out vec4 fragColor, vec2 coord) &#123;
    vec2 uv = coord / iResolution.xy;
    vec2 mouse = iMouse.xy / iResolution.xy;
    float cTime = sin(iTime * SPEED);
    uv = twirl(uv, mouse, Range, Angle * cTime);
    vec4 color = texture(iChannel0, uv);
    fragColor = color;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得一提的是，除了用线性方程表示扭曲关系，还可以使用smoothstep方法，相比linear线性函数，smoothstep方法在扭曲边界处呈现更为平滑，如下图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa299b53f6664845bb1a9742aef56ef9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>linear和smoothstep扭曲方程效果对比</em></p>
<p>考虑到边界的平滑，下面的变形方法也多会用smoothstep函数来替代线性方程。</p>
<h2 data-id="heading-4">膨胀/收缩</h2>
<p>膨胀特点靠近膨胀中心的纹理被拉伸，而靠近膨胀边界纹理被挤压，这意味着在膨胀范围内，以膨胀中心为距离场，每个采样圈都应该比原先的半径更小，并且圈间距由内到外逐渐扩大。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c3ff57698be46eb9107d6f09b154f4a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如下图右侧，我们通过将等距的黑色采样圈映射到更内聚的红色采样圈，使新采样圈之间的间距由内到外单调递增。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14c4124dd08b4743a4794607d657a240~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>膨胀采样距离场变换</em></p>
<p>我们采样平滑递增函数smoothstep来通过采样圈半径dist计算出缩放值scale：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b648e9f1cedc4a18a98735bf155e62c6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图的函数表明，在靠近膨胀中心处，采样圈缩放最明显，缩放值最小(1 - S)；随着dist增大，缩放值scale往1递增，直至到达R边界范围后，scale恒定为1，采样圈不再缩放。</p>
<pre><code class="copyable">float scale = (1.- S) + S * smoothstep(0.,1., dist / R); // 计算膨胀采样半径缩放值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是我们得到上述采样半径缩放公式，其中设定Strength(0 < S < 1)代表膨胀程度。 对于膨胀距离场的变换过程，很容易推断出，要实现膨胀的反向效果收缩，直接让S位于[-1,0]区间即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab27d6b44b004121a3769372c00d1b32~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>S值对应膨胀收缩程度Strength</em></p>
<p>如上图，膨胀函数入参S(变形程度Strength)和R(变形范围Range)可这么描述： 1）当S在[0,1]区间时，呈现膨胀效果，S值越大，膨胀的程度越高； 2）当S在[-10]区间时，呈现收缩效果，S值越小，收缩程度越高； 3）R代表变形的边界，值越大时，影响区域越大；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/260a8c9db88245c581b2eeedd439793c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>动态膨胀效果</em></p>
<p>我们可以引入时间变量time动态改变Strength的值，模拟呼吸动画，如上图小丑鼓肚子效果，具体shader代码如下：</p>
<pre><code class="copyable">#iChannel0 "src/assets/texture/joker.png"
#define SPEED 2. // 速度
#define RANGE .2 // 变形范围
#define Strength .5 * sin(iTime * SPEED) // 变形程度

vec2 inflate(vec2 uv, vec2 center, float range, float strength) &#123;
    float dist = distance(uv , center);
    vec2 dir = normalize(uv - center);
    float scale = 1.-strength + strength * smoothstep(0., 1. ,dist / range);
    float newDist = dist * scale;
    return center + newDist * dir;
&#125;
void mainImage(out vec4 fragColor, vec2 coord) &#123;
    vec2 uv = coord / iResolution.xy;
    vec2 mouse = iMouse.xy / iResolution.xy;
    uv = inflate(uv, mouse, RANGE, Strength);
    vec3 color = texture(iChannel0, uv).rgb;
    fragColor.rgb = color;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">纵向/横向拉伸</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e621a113a6b471bbf5547b3bbae7547~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>原图-纵向拉伸-横向拉伸-膨胀</em></p>
<p>前面的膨胀是通过对距离场采样圈进行缩放实现的，纵向/横向拉伸则是只对采样圈x轴或y轴进行缩放，一般可用在美颜的“长腿特效”上。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0961cd4503f74f26bf6556546afd1f64~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>横向拉伸距离场变换</em></p>
<p>可以发现横向拉伸距离场被变换为多个椭圆采样圈，代码实现如下：</p>
<pre><code class="copyable">vec2 inflateX(vec2 uv, vec2 center, float radius, float strength) &#123;
    // 前面代码跟膨胀实现一样
    ...
    return center + vec2(newDist, dist) * dir; // 横向拉伸则scale只作用于想x轴
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">挤压</h2>
<p>挤压一般会指明一个作用点和一个挤压方向，它的特点是把作用点附近的纹理推到挤压终点位置。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7581194212714961b767741786ae0eac~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如下图，绿色作用点P作为挤压起点，箭头为挤压向量V，其中向量方向指明挤压的方向，向量长度length(V)代表挤压的距离，向量终点为挤压后的位置。 要实现纹理挤压，就是让采样圈圆心往挤压向量V上偏移，采样中心点应平移到点P的位置。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/568d41f21f9248d193b2bef332b1d037~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>挤压采用距离场变换</em></p>
<p>随着采样圈的半径dist由内到外逐渐变大，其变换后的圆心偏移量offset逐渐缩短，我们可以用-smoothstep平滑递减函数处理采样圈半径dist与圈偏移量offset之间的关系。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fdb12c9cb4c40adb1a0b8615343b278~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>公式：offset = length(V) - length(V) * smoothstep(0, R, dist)，其中R表示挤压边界range。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9999261d768f4336ae579c2d5007cf74~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>挤压动态效果</em></p>
<p>同样的，我们引入时间变量time动态改变挤压向量的长度和方向，可以实现抖动特效，如上图小丑顶胯效果，具体shader代码如下：</p>
<pre><code class="copyable">#iChannel0 "src/assets/texture/joker.png"
#define RANGE .25  // 变形范围
#define PINCH_VECTOR vec2( sin(iTime * 10.), cos(iTime * 20.)) * .03 // 挤压向量

vec2 pinch(vec2 uv, vec2 targetPoint, vec2 vector, float range) 
&#123; 
    vec2 center = targetPoint + vector;
    float dist = distance(uv, targetPoint);
    vec2 point = targetPoint +  smoothstep(0., 1., dist / range) * vector;
    return uv - center + point;
&#125;
void mainImage(out vec4 fragColor, vec2 coord) &#123;
    vec2 uv = coord / iResolution.xy;
    vec2 mouse = iMouse.xy / iResolution.xy;
    uv = pinch(uv, mouse, PINCH_VECTOR, RANGE);
    vec3 color = texture(iChannel0, uv).rgb;
    fragColor.rgb = color;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">总结</h2>
<p>本文主要介绍三类局部变形shader的实现原理，其中膨胀/收缩和挤压效果是通过采样距离场变换实现的，前者变换的是采样圈大小，后者变换的是采用圈位置。 除了上文的介绍的三种局部变形，还有一些比较有趣的全局变形效果，比如波浪特效(wave effect)，错位特效和镜像等，shader实现比较容易，就不多做介绍了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc8f9a43f1914f46880660a7f04e0fff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>波浪-错位-镜像</em></p>
<h2 data-id="heading-8">预览代码与效果</h2>
<p>扭曲：<a href="https://www.shadertoy.com/view/slfGzN" target="_blank" rel="nofollow noopener noreferrer">www.shadertoy.com/view/slfGzN</a> 膨胀/缩放：<a href="https://www.shadertoy.com/view/7lXGzN" target="_blank" rel="nofollow noopener noreferrer">www.shadertoy.com/view/7lXGzN</a> 挤压/拉伸：<a href="https://www.shadertoy.com/view/7tX3zN" target="_blank" rel="nofollow noopener noreferrer">www.shadertoy.com/view/7tX3zN</a></p>
<h2 data-id="heading-9">参考资料：</h2>
<p>glsl基础变换：<a href="https://thebookofshaders.com/08/?lan=ch" target="_blank" rel="nofollow noopener noreferrer">thebookofshaders.com/08/?lan=ch</a> Photoshop挤压特效算法：<a href="https://blog.csdn.net/kezunhai/article/details/41873775" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/kezunhai/ar…</a></p>
<h2 data-id="heading-10">传送门</h2>
<p>WebGL进阶——走进图形噪声​：<a href="https://zhuanlan.zhihu.com/p/68507311" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/68507311</a></p></div>  
</div>
            