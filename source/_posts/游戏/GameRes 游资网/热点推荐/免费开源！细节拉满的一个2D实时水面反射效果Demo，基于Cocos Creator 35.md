
---
title: '免费开源！细节拉满的一个2D实时水面反射效果Demo，基于Cocos Creator 3.5'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202207/15/110132ynmmqmqqgqwm7733.gif'
author: GameRes 游资网
comments: false
date: Fri, 15 Jul 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202207/15/110132ynmmqmqqgqwm7733.gif'
---

<div>   
<div class="quote"><blockquote>引言：插件 Easy NavMesh、BenchMark 性能检测的作者孙二喵，从开发者王师傅的论坛分享中获得启发，实现了 2D 实时水面反射效果，Demo 免费开源。</blockquote></div><br>
<strong><font color="#de5650">2D 实时水面反射</font></strong><br>
<br>
<div align="center"><font size="2">
<img aid="1046320" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110132ynmmqmqqgqwm7733.gif" data-original="https://di.gameres.com/attachment/forum/202207/15/110132ynmmqmqqgqwm7733.gif" width="529" id="aimg_1046320" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110132ynmmqmqqgqwm7733.gif" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">Demo 效果</font></div><br>
前几天看到论坛大佬的 2D 水面 Shader 教程（注：后文有详细内容），效果挺好的，就跟着在 Cocos Creator 3.5.2 中做了一个，实现 2D 实时水面反射，并支持角色移动，开箱即用。<br>
<br>
<strong>功能特点</strong><br>
<br>
整个方案使用了3个摄像机：<br>
<br>
RT 摄像机负责所有游戏物体，它会获取 Rendertexture 渲染到地面和水面的2个精灵上。<br>
<br>
<div align="center">
<img aid="1046321" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110132kujp6f4aezjum0fd.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110132kujp6f4aezjum0fd.jpg" width="600" id="aimg_1046321" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110132kujp6f4aezjum0fd.jpg" referrerpolicy="no-referrer">
</div><br>
FixCamera 是固定摄像机，只会拍摄地面和水面这2个精灵。<br>
<br>
<div align="center">
<img aid="1046322" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110132mdtdwsciu88uwcaz.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110132mdtdwsciu88uwcaz.jpg" width="600" id="aimg_1046322" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110132mdtdwsciu88uwcaz.jpg" referrerpolicy="no-referrer">
</div><br>
UI 相机负责 UI 层级。<br>
<br>
最终的 DrawCall 为8个，包括1个基础 DC +1个背景+1个角色+2个技能特效+1个 UI+ 1个水面渲染+1个地面渲染。<br>
<br>
<div align="center">
<img aid="1046323" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110132fn86cj8ejc6jj8ln.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110132fn86cj8ejc6jj8ln.jpg" width="600" id="aimg_1046323" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110132fn86cj8ejc6jj8ln.jpg" referrerpolicy="no-referrer">
</div><br>
即使增加1个新的精灵类，我们整个 DrawCall 也只会增加1个。<br>
<br>
<div align="center">
<img aid="1046324" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110132xcc7dauiioadacbj.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110132xcc7dauiioadacbj.jpg" width="600" id="aimg_1046324" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110132xcc7dauiioadacbj.jpg" referrerpolicy="no-referrer">
</div><br>
针对反射方案，第一个 RT 摄像机负责地面部分的截取，这里把 rect 设置成了 -0.37 , 只截取63%的上半部分屏幕。<br>
<br>
<div align="center">
<img aid="1046325" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110133g04tuzuzm72bhhye.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110133g04tuzuzm72bhhye.png" width="421" id="aimg_1046325" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110133g04tuzuzm72bhhye.png" referrerpolicy="no-referrer">
</div><br>
针对地面部分，我们使用了自定义 Shader，移植了默认的 Sample from RT，使用了和 Canvas 一样的尺寸，针对屏幕适配，Canvas 上的 rtAdapter 里有解决方案。<br>
<br>
<div align="center">
<img aid="1046326" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110133sz55nkkneyayr5ya.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110133sz55nkkneyayr5ya.png" width="600" id="aimg_1046326" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110133sz55nkkneyayr5ya.png" referrerpolicy="no-referrer">
</div><br>
水面部分只使用了一半的屏幕高度，这里加了 Tiling 的 Macro，设置了 UV。<br>
<br>
<div align="center">
<img aid="1046327" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110133mxit4o47oat4ueit.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110133mxit4o47oat4ueit.png" width="600" id="aimg_1046327" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110133mxit4o47oat4ueit.png" referrerpolicy="no-referrer">
</div><br>
水浪效果，通过 update wavetexture 的 uv 得到一个偏移量 offset，并于原始图片的 uv 相加。<br>
<br>
<div align="center">
<img aid="1046328" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110133tz8qrexroqwooj00.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110133tz8qrexroqwooj00.png" width="600" id="aimg_1046328" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110133tz8qrexroqwooj00.png" referrerpolicy="no-referrer">
</div><br>
波浪效果有了，但是看起来比较单一，这里希望水面的颜色更有多彩，同时有一点邪恶的小紫色。<br>
<br>
<div align="center">
<img aid="1046329" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110133bycq3v44f34ry4wq.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110133bycq3v44f34ry4wq.jpg" width="600" id="aimg_1046329" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110133bycq3v44f34ry4wq.jpg" referrerpolicy="no-referrer">
</div><br>
加了 casutic 效果后，水面有了焦散的流动。<br>
<br>
<div align="center">
<img aid="1046330" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110134se77eecxux87cdz7.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110134se77eecxux87cdz7.png" width="600" id="aimg_1046330" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110134se77eecxux87cdz7.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1046331" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110134ped9uo9e417ga27g.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110134ped9uo9e417ga27g.jpg" width="600" id="aimg_1046331" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110134ped9uo9e417ga27g.jpg" referrerpolicy="no-referrer">
</div><br>
为了让水面底部看起来颜色更深，这里使用了 smoothstep 根据 uv.y 做变化。<br>
<br>
<div align="center">
<img aid="1046332" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110134wa814k89v8gs7rgr.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110134wa814k89v8gs7rgr.png" width="481" id="aimg_1046332" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110134wa814k89v8gs7rgr.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1046333" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110134ny3ujgct8g3c8jcf.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110134ny3ujgct8g3c8jcf.jpg" width="600" id="aimg_1046333" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110134ny3ujgct8g3c8jcf.jpg" referrerpolicy="no-referrer">
</div><br>
为了让水面上部看起来更通透，彷佛有水波打到岸，对透明度也使用了 smoothstep。<br>
<br>
<div align="center">
<img aid="1046334" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110134ps6bi63s93t3jp8z.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110134ps6bi63s93t3jp8z.png" width="460" id="aimg_1046334" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110134ps6bi63s93t3jp8z.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1046335" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110135b66ewqtqtqrwzrtq.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110135b66ewqtqtqrwzrtq.jpg" width="600" id="aimg_1046335" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110135b66ewqtqtqrwzrtq.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1046336" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110135mpypppt1kuo1ifrp.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110135mpypppt1kuo1ifrp.png" width="407" id="aimg_1046336" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110135mpypppt1kuo1ifrp.png" referrerpolicy="no-referrer">
</div><br>
最后给小姐姐加上一个 FSM 状态机和一个 spriteatlas 的 animator controller，就可以拖到摇杆跑起来啦！<br>
<br>
<div align="center">
<img aid="1046337" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110135xmoozh7zmjaxjopo.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110135xmoozh7zmjaxjopo.jpg" width="600" id="aimg_1046337" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110135xmoozh7zmjaxjopo.jpg" referrerpolicy="no-referrer">
</div><br>
这里要注意的是，我只移动了 RT 相机，没有移动水面的 renderer，所以水面会看起来比较奇怪，可以在人物移动的时候，给水面的水波和焦散一个反方向（下次一定，下次一定）。<br>
<br>
<strong>资源链接</strong><br>
<br>
<strong>点击文末【阅读原文】下载 Demo：</strong><br>
https://store.cocos.com/app/detail/3900<br>
<br>
<strong>论坛专贴：</strong><br>
https://forum.cocos.org/t/topic/137681<br>
<br>
<strong><font color="#de5650">实现过程</font></strong><br>
<br>
以下为社区开发者「王师傅」发布在论坛的技术分享。作者花式使用噪声图实现了 2D 水面波浪效果，这也是上文孙二喵 Demo 的方案参考，感兴趣的小伙伴可以阅读一下。帖子地址：<br>
<br>
https://forum.cocos.org/t/topic/121407<br>
<br>
<div align="center"><font size="2">
<img aid="1046338" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110135c30d663e9e42puup.gif" data-original="https://di.gameres.com/attachment/forum/202207/15/110135c30d663e9e42puup.gif" width="581" id="aimg_1046338" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110135c30d663e9e42puup.gif" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">最终效果</font></div><br>
<strong>场景准备</strong><br>
<br>
首先弄个干净的 Shader，然后布个游戏场景。<br>
<br>
<div align="center"><font size="2">
<img aid="1046339" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110135na5naac61l126m4a.jpg" data-original="https://di.gameres.com/attachment/forum/202207/15/110135na5naac61l126m4a.jpg" width="600" id="aimg_1046339" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110135na5naac61l126m4a.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">主场景图</font></div><div align="center"><font size="2"><br>
</font></div><div align="center"><font size="2">
<img aid="1046340" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110136s3y5x7ppabbxgi5i.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110136s3y5x7ppabbxgi5i.png" width="600" id="aimg_1046340" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110136s3y5x7ppabbxgi5i.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">反转y轴，放在下方做水面用的</font></div><div align="center"><font size="2"><br>
</font></div><div align="center"><font size="2">
<img aid="1046341" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110136eks37k9tt8shquh0.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110136eks37k9tt8shquh0.png" width="600" id="aimg_1046341" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110136eks37k9tt8shquh0.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">摆一下场景</font></div><br>
NewSprite 缩放是 -0.55 ，负数是为了反转 y 轴做镜像效果。<br>
<br>
NewSprite 用上我们新建的干净的 Shader 和材质，Shader 删掉片元着色器我们不准备用的代码，老规矩，从一张黑图开始。<br>
<br>
precision highp float;<br>
<br>
#include <alpha-test><br>
<br>
#include <texture><br>
<br>
#include <cc-global><br>
<br>
in vec4 v_color;<br>
<br>
#if USE_TEXTURE<br>
<br>
in vec2 v_uv0;<br>
<br>
uniform sampler2D texture;<br>
<br>
#endif<br>
<br>
void main () &#123;<br>
<br>
vec3 color = vec3(0.);<br>
<br>
// 弄个t接收cc_time.x, *= 0.6是因为正常速太快，变慢点 备用<br>
<br>
float t = cc_time.x * 0.6;<br>
<br>
gl_FragColor = vec4(color,1.);<br>
<br>
&#125;<br>
<br>
<div align="center">
<img aid="1046342" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110136o6cc2lf1h40hnc4c.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110136o6cc2lf1h40hnc4c.png" width="600" id="aimg_1046342" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110136o6cc2lf1h40hnc4c.png" referrerpolicy="no-referrer">
</div><br>
<strong>噪声图</strong><br>
<br>
准备一张噪声图：<br>
<br>
<div align="center">
<img aid="1046343" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110136hmzmwbkccqzzvgxm.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110136hmzmwbkccqzzvgxm.png" width="512" id="aimg_1046343" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110136hmzmwbkccqzzvgxm.png" referrerpolicy="no-referrer">
</div><br>
// 文件开头修改加入texture2的声明<br>
<br>
properties:<br>
<br>
texture: &#123; value: white &#125;<br>
<br>
// 添加下面的行 本行注释删掉，写在这里只是为了标识这是添加的<br>
<br>
texture2: &#123;  value: white &#125;<br>
<br>
....<br>
<br>
....<br>
<br>
// 片元着色器修改成下面这样：<br>
<br>
.....<br>
<br>
uniform sampler2D texture;<br>
<br>
// 添加下面的行<br>
<br>
uniform sampler2D texture2;<br>
<br>
void main () &#123;<br>
<br>
vec3 color = vec3(0.);<br>
<br>
// 弄个t接收cc_time.x, *= 0.6是因为正常速太快，变慢点<br>
<br>
float t = cc_time.x * 0.6;<br>
<br>
// 对噪声图取样x通道，显示在屏幕上<br>
<br>
color += texture2D(texture2,v_uv0).x;<br>
<br>
gl_FragColor = vec4(color,1.);<br>
<br>
&#125;<br>
<br>
然后打开点击材质，把噪声图拖拽到材质面板中的 texture2 中。看下现在的样子：<br>
<br>
<div align="center">
<img aid="1046344" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110137xlvsyowkzpdsyfaz.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110137xlvsyowkzpdsyfaz.png" width="600" id="aimg_1046344" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110137xlvsyowkzpdsyfaz.png" referrerpolicy="no-referrer">
</div><br>
<strong>水波效果</strong><br>
<br>
接着我们用这个噪声图实现水波荡漾的效果。取噪声图的 xy 两个通道，作为对场景图取样所用 uv 的偏移值，会出来什么效果呢？<br>
<br>
片元着色器 main 函数改成下面这样：<br>
<br>
void main () &#123;<br>
<br>
vec3 color = vec3(0.);<br>
<br>
// 弄个t接收cc_time.x, *= 0.6是因为正常速太快，变慢点<br>
<br>
float t = cc_time.x * 0.6;<br>
<br>
// + t * vec2(.5,.1)<br>
<br>
vec2 off1 = texture2D(texture2,v_uv0).xy;<br>
<br>
// 偏移值缩放0.1倍，不然波纹太过分了<br>
<br>
off1 *= .1;<br>
<br>
color += texture2D(texture,off1 + v_uv0).xyz;<br>
<br>
gl_FragColor = vec4(color,1.);<br>
<br>
&#125;<br>
<br>
<div align="center">
<img aid="1046376" zoomfile="https://di.gameres.com/attachment/forum/202207/15/111018z9tdh9tymsy00dt3.png" data-original="https://di.gameres.com/attachment/forum/202207/15/111018z9tdh9tymsy00dt3.png" width="600" id="aimg_1046376" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/111018z9tdh9tymsy00dt3.png" referrerpolicy="no-referrer">
</div><br>
可以看到，画面明显扭曲了，但是现在还是静态的，需要加入时间参数让这个扭曲动起来。<br>
<br>
偏移值的0.1的缩放值还是太大，下面用0.01的试试：<br>
<br>
void main () &#123;<br>
<br>
vec3 color = vec3(0.);<br>
<br>
// 弄个t接收cc_time.x, *= 0.6是因为正常速太快，变慢点<br>
<br>
float t = cc_time.x * 0.6;<br>
<br>
// v_uv0 + t * vec2(.5,.1) 这里的t是上面的时间，会持续增大的一个数值<br>
<br>
// vec2(.5,.1) 是我随便写的一个方向向量，方向*时间 作为uv的偏移<br>
<br>
// 噪声图设置 WrapMode = Repeat 否则偏移值超过vec2(1.,1.)之后就取不到值了，要改成repeat才可以取值<br>
<br>
vec2 off1 = texture2D(texture2,v_uv0 + t * vec2(.5,.1)).xy;<br>
<br>
// 偏移值缩放0.1倍，不然波纹太过分了<br>
<br>
off1 *= .01;<br>
<br>
color += texture2D(texture,off1 + v_uv0).xyz;<br>
<br>
gl_FragColor = vec4(color,1.);<br>
<br>
&#125;<br>
<br>
<div align="center">
<img aid="1046345" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110137yzd30928a88t91to.gif" data-original="https://di.gameres.com/attachment/forum/202207/15/110137yzd30928a88t91to.gif" width="180" id="aimg_1046345" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110137yzd30928a88t91to.gif" referrerpolicy="no-referrer">
</div><br>
现在，水面波动已经明显了。<br>
<br>
<strong>水面明暗</strong><br>
<br>
接着实现一下水面的明暗变化，镜头越近颜色越暗（其实就是屏幕越往下变颜色越黑）。<br>
<br>
color += texture2D(texture,off1 + v_uv0).xyz;<br>
<br>
// 参数0-1是正好 从黑到白的，用-.5->1.3这个范围，色值就是不太黑到不太白，免得颜色太极端<br>
<br>
color *= smoothstep(-.5,1.3,v_uv0.y) - .3;<br>
<br>
<div align="center">
<img aid="1046346" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110137el5ud9d7uu522c13.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110137el5ud9d7uu522c13.png" width="600" id="aimg_1046346" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110137el5ud9d7uu522c13.png" referrerpolicy="no-referrer">
</div><br>
<strong>水面浮沫</strong><br>
<br>
添加一些水面的浮沫，丰富细节。<br>
<br>
这里又要用噪声图了。我们对噪声图再来一次取值：<br>
<br>
// baseuv做变换对噪声图取值<br>
<br>
vec2 baseuv = v_uv0;<br>
<br>
// 让噪声图x轴重复四次，y轴重复三次<br>
<br>
vec2 scale = vec2(4.,3.);<br>
<br>
baseuv = baseuv * scale;<br>
<br>
float c1 = texture2D(texture2,baseuv).x;<br>
<br>
color = vec3(c1);<br>
<br>
gl_FragColor = vec4(color,1.);<br>
<br>
<div align="center">
<img aid="1046347" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110138i16es55sjeezh5pc.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110138i16es55sjeezh5pc.png" width="600" id="aimg_1046347" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110138i16es55sjeezh5pc.png" referrerpolicy="no-referrer">
</div><br>
现在看着像海浪，并不是我们想要的浮沫效果。怎么从这个海浪变换一个浮沫的效果出来呢？<br>
<br>
float c1 = texture2D(texture2,baseuv).x;<br>
<br>
// 加这一行<br>
<br>
c1 = smoothstep(0.23,0.,c1);<br>
<br>
color = vec3(c1);<br>
<br>
<div align="center">
<img aid="1046348" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110138ngf0417nv1v4c9gn.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110138ngf0417nv1v4c9gn.png" width="600" id="aimg_1046348" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110138ngf0417nv1v4c9gn.png" referrerpolicy="no-referrer">
</div><br>
啥原理呢，上面那个大浪啊，值0-1的，用 smoothstep 对大浪做个变换，只留下 0-0.23 的色值，大于 0.23 的都变成了纯黑色。<br>
<br>
大概画一个函数曲线：<br>
<br>
<div align="center">
<img aid="1046349" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110138ri797pgvpitpsvm7.png" data-original="https://di.gameres.com/attachment/forum/202207/15/110138ri797pgvpitpsvm7.png" width="214" id="aimg_1046349" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110138ri797pgvpitpsvm7.png" referrerpolicy="no-referrer">
</div><br>
c1 值输入函数曲线后，0-0.23范围输出了 0->1 的值，越黑的地方越亮，亮的就变黑色了，也就得到了上面图的效果。<br>
<br>
接着让浮沫漂流起来。思考一下，如果让浮沫整体往一个方向漂是不是有点太单调太假了，不行，要做分行速度差。分20行吧，每行做移动速度不同的漂流：<br>
<br>
float random (vec2 st) &#123;<br>
<br>
return fract(sin(dot(st.xy,<br>
<br>
vec2(12.9898,78.233)))*<br>
<br>
43758.5453123);<br>
<br>
&#125;<br>
<br>
......<br>
<br>
上面的函数加在main函数外面<br>
<br>
下面的东西是main里面的<br>
<br>
......<br>
<br>
// 白沫的uv 所以取名mouv!<br>
<br>
vec2 mouv = v_uv0;<br>
<br>
// 做y轴分行，原理见彩虹那篇帖子<br>
<br>
mouv.y *= 20.;<br>
<br>
// n3就是行id 取名无力<br>
<br>
float n3 = floor(mouv.y);<br>
<br>
// n4就是用行id随机一个对应的随机值出来，每行一个随机值作为行的运动速度<br>
<br>
// 所以对于y轴在同一行（注意上面*=20，所以共20行），我们这里计算出一个改行的运动速度，放在这备用<br>
<br>
float n4 = random(vec2(n3,n3)) + .3;<br>
<br>
// baseuv做变换对噪声图取值<br>
<br>
vec2 baseuv = v_uv0;<br>
<br>
// 让噪声图x轴重复四次，y轴重复三次<br>
<br>
vec2 scale = vec2(4.,3.);<br>
<br>
baseuv = baseuv * scale;<br>
<br>
// 取值用的uv加上向左的移动 t是上面用过的那个cc_time.x哈，*0.1不然太快了<br>
<br>
// n4是上面计算好的速度哈<br>
<br>
baseuv.x += t * .1 * n4;<br>
<br>
float c1 = texture2D(texture2,baseuv).x;<br>
<br>
c1 = smoothstep(0.23,0.,c1);<br>
<br>
color = vec3(c1);<br>
<br>
<div align="center">
<img aid="1046350" zoomfile="https://di.gameres.com/attachment/forum/202207/15/110138rqqjpmvevq2imbmq.gif" data-original="https://di.gameres.com/attachment/forum/202207/15/110138rqqjpmvevq2imbmq.gif" width="180" id="aimg_1046350" inpost="1" src="https://di.gameres.com/attachment/forum/202207/15/110138rqqjpmvevq2imbmq.gif" referrerpolicy="no-referrer">
</div><br>
<strong>最终效果</strong><br>
<br>
综合上述几个实现后，我们得到了最终的呈现效果，完整代码：<br>
<br>
// Copyright (c) 2017-2018 Xiamen Yaji Software Co., Ltd.<br>
<br>
CCEffect %&#123;<br>
<br>
techniques:<br>
<br>
- passes:<br>
<br>
- vert: vs<br>
<br>
frag: fs<br>
<br>
blendState:<br>
<br>
targets:<br>
<br>
- blend: true<br>
<br>
rasterizerState:<br>
<br>
cullMode: none<br>
<br>
properties:<br>
<br>
texture: &#123; value: white &#125;<br>
<br>
texture2: &#123;  value: white &#125;<br>
<br>
alphaThreshold: &#123; value: 0.5 &#125;<br>
<br>
&#125;%<br>
<br>
CCProgram vs %&#123;<br>
<br>
precision highp float;<br>
<br>
#include <cc-global><br>
<br>
#include <cc-local><br>
<br>
in vec3 a_position;<br>
<br>
in vec4 a_color;<br>
<br>
out vec4 v_color;<br>
<br>
#if USE_TEXTURE<br>
<br>
in vec2 a_uv0;<br>
<br>
out vec2 v_uv0;<br>
<br>
#endif<br>
<br>
void main () &#123;<br>
<br>
vec4 pos = vec4(a_position, 1);<br>
<br>
#if CC_USE_MODEL<br>
<br>
pos = cc_matViewProj * cc_matWorld * pos;<br>
<br>
#else<br>
<br>
pos = cc_matViewProj * pos;<br>
<br>
#endif<br>
<br>
#if USE_TEXTURE<br>
<br>
v_uv0 = a_uv0;<br>
<br>
#endif<br>
<br>
v_color = a_color;<br>
<br>
gl_Position = pos;<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
CCProgram fs %&#123;<br>
<br>
precision highp float;<br>
<br>
#include <alpha-test><br>
<br>
#include <texture><br>
<br>
#include <cc-global><br>
<br>
in vec4 v_color;<br>
<br>
in vec2 v_uv0;<br>
<br>
uniform sampler2D texture;<br>
<br>
uniform sampler2D texture2;<br>
<br>
float random (vec2 st) &#123;<br>
<br>
return fract(sin(dot(st.xy,<br>
<br>
vec2(12.9898,78.233)))*<br>
<br>
43758.5453123);<br>
<br>
&#125;<br>
<br>
void main () &#123;<br>
<br>
vec3 color = vec3(0.);<br>
<br>
// 弄个t接收cc_time.x, *= 0.6是因为正常速太快，变慢点<br>
<br>
float t = cc_time.x * 0.6;<br>
<br>
// v_uv0 + t * vec2(.5,.1) 这里的t是上面的时间，会持续增大的一个数值<br>
<br>
// vec2(.5,.1) 是我随便写的一个方向向量，方向*时间 作为uv的偏移<br>
<br>
// 噪声图设置 WrapMode = Repeat 否则偏移值超过vec2(1.,1.)之后就取不到值了，要改成repeat才可以取值<br>
<br>
vec2 off1 = texture2D(texture2,v_uv0 + t * vec2(.5,.1)).xy;<br>
<br>
// 偏移值缩放0.1倍，不然波纹太过分了<br>
<br>
off1 *= .01;<br>
<br>
color += texture2D(texture,off1 + v_uv0).xyz;<br>
<br>
// 参数0-1是正好 从黑到白的，用-.5->1.3这个范围，色值就是不太黑到不太白，免得颜色太极端<br>
<br>
color *= smoothstep(-.5,1.3,v_uv0.y) - .3;<br>
<br>
// 白沫的uv 所以取名mouv!<br>
<br>
vec2 mouv = v_uv0;<br>
<br>
// 做y轴分行，原理见彩虹那篇帖子<br>
<br>
mouv.y *= 20.;<br>
<br>
// n3就是行id 取名无力<br>
<br>
float n3 = floor(mouv.y);<br>
<br>
// n4就是用行id随机一个对应的随机值出来，每行一个随机值作为行的运动速度<br>
<br>
// 所以对于y轴在同一行（注意上面*=20，所以共20行），我们这里计算出一个改行的运动速度，放在这备用<br>
<br>
float n4 = random(vec2(n3,n3)) + .3;<br>
<br>
// baseuv做变换对噪声图取值<br>
<br>
vec2 baseuv = v_uv0;<br>
<br>
// 让噪声图x轴重复四次，y轴重复三次<br>
<br>
vec2 scale = vec2(4.,3.);<br>
<br>
baseuv = baseuv * scale;<br>
<br>
// 取值用的uv加上向左的移动 t是上面用过的那个cc_time.x哈，*0.1不然太快了<br>
<br>
// n4是上面计算好的速度哈<br>
<br>
baseuv.x += t * .1 * n4;<br>
<br>
float c1 = texture2D(texture2,baseuv).x;<br>
<br>
c1 = smoothstep(0.23,0.,c1);<br>
<br>
color += vec3(c1);<br>
<br>
gl_FragColor = vec4(color,1.);<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
<font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/o319kxdbEunkQsloDu0rEA</font><br>
<br>
<br>
  
</div>
            