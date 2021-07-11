
---
title: '鸿蒙应用开发 _ 揭开神秘 开关（Switch）的功能与用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e15ea25a430348c6a3ddf8945b7f5557~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 05:57:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e15ea25a430348c6a3ddf8945b7f5557~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<blockquote>
<p>导语：大家好，我是你们的朋友 朋哥，最近开发鸿蒙多了有很多发现，鸿蒙不仅在系统层面做了很多用户体验优化，应用层也做了很大的优化，对于开发者，鸿蒙做了很多提供给开发者的便利，后面一一道来。</p>
</blockquote>
<p>上一篇原创文章 解析了 复选框 Chexkbox的功能和用法。也把这个功能用到了鸿蒙开发的知乎登录页面。</p>
<p>各位尽快学习，后面更新会比较快了，现在是为了给新学习的一点事件来敢。</p>
<p>好了，来说一下今天的重点......</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e15ea25a430348c6a3ddf8945b7f5557~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>下面我们开始今天的文章，还是老规矩，通过如下几点来说：</p>
<blockquote>
<p>1，简介<br>
2，用到的属性<br>
3，实战</p>
</blockquote>
<h3 data-id="heading-0">简介</h3>
<p>Switch是一个可以在两种状态切换的开关控件。只有开关两种状态。</p>
<p>一般引用在手机应用的设置界面 做一些开关操作，或者某一个功能的开关操作。</p>
<h3 data-id="heading-1">用到的属性</h3>
<p>Switch的共有XML属性还是继承自：Text</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6631237df004b5cae3225b52c792475~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>属性中 有两个比较重要 ：</strong></p>
<p>text_state_on // 开启显示的文本<br>
text_state_off //关闭显示的文本</p>
<h3 data-id="heading-2">实战</h3>
<p>先来创建一个基本的开关试试把。<br>
1，开关默认效果</p>
<pre><code class="copyable"><Switch
    ohos:id="$+id:switch_opt"
    ohos:height="match_content"
    ohos:width="match_content"
    ohos:text_state_off="关闭"
    ohos:text_state_on="开启"
    ohos:padding="5vp"
    ohos:text_size="16fp"
    />
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">1，默认效果 添加了 几个属性，开启和关闭文字，字体大小</p>
<p>查看一下效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c70e39cbd4bf4501bb5c697555bfc159~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>2，设置背景样式</p>
<pre><code class="copyable">ShapeElement elementThumbOn = new ShapeElement();
elementThumbOn.setShape(ShapeElement.OVAL);
elementThumbOn.setRgbColor(RgbColor.fromArgbInt(0xFF1E90FF));
elementThumbOn.setCornerRadius(50);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">1，设置背景演示和圆角</p>
<p>3，设置背景状态</p>
<pre><code class="copyable">// 滑块样式的设置
private StateElement trackElementInit(ShapeElement on, ShapeElement off)&#123;
    StateElement trackElement = new StateElement();
    trackElement.addState(new int[]&#123;ComponentState.COMPONENT_STATE_CHECKED&#125;, on);
    trackElement.addState(new int[]&#123;ComponentState.COMPONENT_STATE_EMPTY&#125;, off);
    return trackElement;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>1. 设置状态，状态是两种背景样式设置的切换</p>
<p>完整代码：</p>
<pre><code class="copyable"><?xml version="1.0" encoding="utf-8"?>
<DirectionalLayout
    xmlns:ohos="http://schemas.huawei.com/res/ohos"
    ohos:height="match_parent"
    ohos:width="match_parent"
    ohos:alignment="center"
    ohos:orientation="vertical">

    <Switch
        ohos:id="$+id:switch_opt"
        ohos:height="match_content"
        ohos:width="match_content"
        ohos:text_state_off="关闭"
        ohos:text_state_on="开启"
        ohos:padding="5vp"
        ohos:text_size="16fp"
        />

</DirectionalLayout>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p>代码逻辑：</p>
<pre><code class="copyable">package com.example.aswitch.slice;

import com.example.aswitch.ResourceTable;
import ohos.aafwk.ability.AbilitySlice;
import ohos.aafwk.content.Intent;
import ohos.agp.colors.RgbColor;
import ohos.agp.components.ComponentState;
import ohos.agp.components.Switch;
import ohos.agp.components.element.ShapeElement;
import ohos.agp.components.element.StateElement;

public class MainAbilitySlice extends AbilitySlice &#123;
    @Override
    public void onStart(Intent intent) &#123;
        super.onStart(intent);
        super.setUIContent(ResourceTable.Layout_ability_main);

        // 开启状态下滑块的样式
        ShapeElement elementThumbOn = new ShapeElement();
        elementThumbOn.setShape(ShapeElement.OVAL);
        elementThumbOn.setRgbColor(RgbColor.fromArgbInt(0xFF1E90FF));
        elementThumbOn.setCornerRadius(50);

        // 关闭状态下滑块的样式
        ShapeElement elementThumbOff = new ShapeElement();
        elementThumbOff.setShape(ShapeElement.OVAL);
        elementThumbOff.setRgbColor(RgbColor.fromArgbInt(0xFFFFFFFF));
        elementThumbOff.setCornerRadius(50);

        // 开启状态下轨迹样式
        ShapeElement elementTrackOn = new ShapeElement();
        elementTrackOn.setShape(ShapeElement.RECTANGLE);
        elementTrackOn.setRgbColor(RgbColor.fromArgbInt(0xFF87CEFA));
        elementTrackOn.setCornerRadius(50);

        // 关闭状态下轨迹样式
        ShapeElement elementTrackOff = new ShapeElement();
        elementTrackOff.setShape(ShapeElement.RECTANGLE);
        elementTrackOff.setRgbColor(RgbColor.fromArgbInt(0xFF808080));
        elementTrackOff.setCornerRadius(50);


        // 设置切换属性
        Switch btnSwitch = (Switch) findComponentById(ResourceTable.Id_switch_opt);
        btnSwitch.setTrackElement(trackElementInit(elementTrackOn, elementTrackOff));
        btnSwitch.setThumbElement(thumbElementInit(elementThumbOn, elementThumbOff));
    &#125;

    // 滑块样式的设置
    private StateElement trackElementInit(ShapeElement on, ShapeElement off)&#123;
        StateElement trackElement = new StateElement();
        trackElement.addState(new int[]&#123;ComponentState.COMPONENT_STATE_CHECKED&#125;, on);
        trackElement.addState(new int[]&#123;ComponentState.COMPONENT_STATE_EMPTY&#125;, off);
        return trackElement;
    &#125;
    // 轨迹样式的设置
    private StateElement thumbElementInit(ShapeElement on, ShapeElement off) &#123;
        StateElement thumbElement = new StateElement();
        thumbElement.addState(new int[]&#123;ComponentState.COMPONENT_STATE_CHECKED&#125;, on);
        thumbElement.addState(new int[]&#123;ComponentState.COMPONENT_STATE_EMPTY&#125;, off);
        return thumbElement;
    &#125;

    @Override
    public void onActive() &#123;
        super.onActive();
    &#125;

    @Override
    public void onForeground(Intent intent) &#123;
        super.onForeground(intent);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a48a3e45ff34f07a2070dd949ce94cc~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>老规矩 代码不能少，要不然小伙伴该说我小气了。<br>
源码：<br>
Switch ： <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fcodegrowth%2Fhaomony-develop%2Ftree%2Fmaster%2FSwitch" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/codegrowth/haomony-develop/tree/master/Switch" ref="nofollow noopener noreferrer">gitee.com/codegrowth/…</a></strong></p>
<p>关注公众号【<strong>程序员漫话编程</strong>】，后台回复 <strong>”鸿蒙“</strong> ，<strong>即可获得上千鸿蒙开源组件。</strong></p>
<blockquote>
<p>原创不易，有用就关注一下。要是帮到了你 就给个三连吧，多谢支持。</p>
</blockquote>
<p><strong>觉得不错的小伙伴，记得帮我</strong> 点个赞和关注哟，笔芯笔芯~**</p>
<blockquote>
<p>作者：码工</p>
</blockquote>
<p>有问题请留言或者私信，可以 微信搜索：<strong>程序员漫话编程</strong>，关注公众号获得更多免费学习资料。</p></div>  
</div>
            