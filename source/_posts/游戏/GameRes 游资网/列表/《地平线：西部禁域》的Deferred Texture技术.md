
---
title: '《地平线：西部禁域》的Deferred Texture技术'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202205/20/092318wxgqg5tnqb4nzb4q.jpg'
author: GameRes 游资网
comments: false
date: Fri, 20 May 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202205/20/092318wxgqg5tnqb4nzb4q.jpg'
---

<div>   
导语：《地平线：西部禁域》是Guerrilla Games在2022年推出的一款备受关注的续作游戏，在游戏当中主角埃洛伊踏上了前往西方未知土地的冒险，为了实现广阔世界的种种表现效果，研发团队对其渲染管线进行了升级优化，其中就包括了Deferred Texture技术。本文内容源于在GDC 2022上Guerrilla Games团队所做的分享，原题为Adventures with Deferred Texturing in 'Horizon Forbidden West' 。<br>
<br>
<div align="center">
<img aid="1040218" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092318wxgqg5tnqb4nzb4q.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092318wxgqg5tnqb4nzb4q.jpg" width="600" id="aimg_1040218" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092318wxgqg5tnqb4nzb4q.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font color="#de5650">overview</font></div><br>
<div align="center">
<img aid="1040219" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092319n3l3rbnr3eplu7un.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092319n3l3rbnr3eplu7un.jpg" width="600" id="aimg_1040219" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092319n3l3rbnr3eplu7un.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">一、关于visibility buffer</font></strong><br>
<br>
visibility buffer其实出来很长时间了，近期通过nanite被大家熟知。它有很多变种，如文章中所列，Intel（原版）、Dawn Engine(Eidos)、UE5、Activision都有不同的做法。<br>
<br>
总的说来就是开始渲染是一个比传统gbuffer小的多的visibility buffer，仅保存primitive id等少量信息，贴图等一概不读。然后再来一个pass，把各种复杂信息补上，输出gbuffer或者直接shading都可以。这个shading过程常常是在compute shader里做的。<br>
<br>
<strong>传统渲染管线的问题</strong><br>
<br>
我们以最标准的vs-rasterize-ps流程来看，这里有若干问题：<br>
<br>
<ul><li>ps总是以2x2 quad来渲染，对于tiny triangle的case，overhead非常高。</li><li>渲染管线非常的“死”，导致很多时候出现大量gap，比如做shadow depth pass的时候，gpu中大量单元非常空闲；老的流程在面临现在更加复杂的case，真的是越来越不给力了。</li><li>async compute等需要进一步挖掘来提升gpu利用率。<br>
</li></ul><br>
<strong>visibility buffer的优势</strong><br>
<br>
<ul><li>实际shading更少的pixel。</li><li>可以各种batch，大幅度提升cache效率。</li><li>可以使用compute shader，async compute，进一步提升gpu的利用率。<br>
</li></ul><br>
<strong><font color="#de5650">二、Guerrilla Games的做法</font></strong><br>
<br>
<strong>overview亮点</strong><br>
<br>
<ul><li>用于植被，相比很多visibility buffer做法用于static mesh，这里是多了一个进步。</li><li>使用IndirectDispatch来进一步做了batch，大幅度提升了wave的利用率。</li><li>融合了自己实现的VRS（不是使用硬件的）。</li><li>完整的管线介绍，和足够有说服力的性能提升。<br>
</li></ul><br>
<strong>植被</strong><br>
<br>
首先guerrilla在horizon里是把visibility buffer用于植被的。<br>
<br>
<div align="center">
<img aid="1040220" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092319e59uw9ox33oqaxfs.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092319e59uw9ox33oqaxfs.jpg" width="600" id="aimg_1040220" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092319e59uw9ox33oqaxfs.jpg" referrerpolicy="no-referrer">
</div><br>
因为植被是一直动的，而且风动动画也一直比较消耗，所以在整个过程中带来挑战：降低vertex transform就格外的重要。<br>
<br>
<strong>技术细节</strong><br>
<br>
visibility buffer的格式：<br>
<br>
<div align="center">
<img aid="1040221" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092319szl49u9h4lbv4hgz.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092319szl49u9h4lbv4hgz.jpg" width="466" id="aimg_1040221" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092319szl49u9h4lbv4hgz.jpg" referrerpolicy="no-referrer">
</div><br>
存的是一个32bit的信息，相比ue和activision的都更小。<br>
<br>
<strong><font color="#de5650">pipeline & batch</font></strong><br>
<br>
<strong>batch</strong><br>
<br>
<div align="center">
<img aid="1040222" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092319ijnl8awkvmwkabli.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092319ijnl8awkvmwkabli.jpg" width="600" id="aimg_1040222" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092319ijnl8awkvmwkabli.jpg" referrerpolicy="no-referrer">
</div><br>
如果我们建好visibility buffer，然后一个compute shader上去算，那么就会出现大量的divergence，导致性能很差。<br>
<br>
这里使用一个DispatchIndirect，先对visibility buffer的内容进行排序，pack到16x16的tile中，然后在发起wave cmd。<br>
<br>
这样的话，shader、texture、const的切换就大大降低，效率提升了不少。<br>
<br>
<strong>vertex transform</strong><br>
<br>
这里visibility一种做法就是在shading pixel的时候，直接做vertex的transform。<br>
<br>
这个如果triangle特别小的话，也可以是一个选项。<br>
<br>
但是horizon的case是，triangle往往还比较大的，那么就还是batc起来比较好。<br>
<br>
就是把要transform的vertex输出到一个ring buffer里，batch&去重，然后计算好了之后再使用。<br>
<br>
<strong>pipeline</strong><br>
<br>
<div align="center">
<img aid="1040223" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092320hzbfkaeuz1iui5ak.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092320hzbfkaeuz1iui5ak.jpg" width="600" id="aimg_1040223" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092320hzbfkaeuz1iui5ak.jpg" referrerpolicy="no-referrer">
</div><br>
整个过程拆得比较细，用到的时候再查就好，道理就是如此。<br>
<br>
<div align="center">
<img aid="1040224" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092320rvkl3vpzyp4pm84z.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092320rvkl3vpzyp4pm84z.jpg" width="600" id="aimg_1040224" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092320rvkl3vpzyp4pm84z.jpg" referrerpolicy="no-referrer">
</div><br>
在pipeline中间可以看到，基本都用async compute把计算给hide起来了。<br>
<br>
<strong>性能</strong><br>
<br>
<div align="center">
<img aid="1040225" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092320jp5f3xfaf23fq88p.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092320jp5f3xfaf23fq88p.jpg" width="535" id="aimg_1040225" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092320jp5f3xfaf23fq88p.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1040226" zoomfile="https://di.gameres.com/attachment/forum/202205/20/092320x2ll4x5teeuwz5b0.jpg" data-original="https://di.gameres.com/attachment/forum/202205/20/092320x2ll4x5teeuwz5b0.jpg" width="532" id="aimg_1040226" inpost="1" src="https://di.gameres.com/attachment/forum/202205/20/092320x2ll4x5teeuwz5b0.jpg" referrerpolicy="no-referrer">
</div><br>
可以看到在这个管线里，性能提升还是很可观的。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：腾讯游戏学堂</font></font><br>
<br>
  
</div>
            