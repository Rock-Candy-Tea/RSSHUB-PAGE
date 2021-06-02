
---
title: '如何评价 6 月 2 日凌晨开源的 OpenHarmony 2.0 Canary_'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=2879'
author: 知乎
comments: false
date: Wed, 02 Jun 2021 09:00:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=2879'
---

<div>   
justjavac的回答<br><br><p>看了几篇最新的鸿蒙文章，还有开放原子的文章，也下载了 2.0 的代码。直到今天下午我才搞清楚了一件事儿：OpenHarmony 是鸿蒙，也不是鸿蒙。OpenHarmony 目前属于开放原子基金会，可以类比为 Chromium。而 HarmonyOS 是华为在 OpenHarmony 之上做的操作系统，可以类比为 Chrome/Edge。OpenHarmony 是自主研发，不兼容 Android。而 6 月 2 日开始向华为手机推送的是 HarmonyOS，而 HarmonyOS 是可以运行 Android App 的。</p><p>整体代码情况 <code>loc --exclude 'third_party|vendor|docs|build|kernel'</code>：</p><div class="highlight"><pre><code class="language-js"><span><span class="o">--------------------------------------------------------------------------------</span>
 <span class="nx">Language</span>             <span class="nx">Files</span>        <span class="nx">Lines</span>        <span class="nx">Blank</span>      <span class="nx">Comment</span>         <span class="nx">Code</span>
<span class="o">--------------------------------------------------------------------------------</span>
 <span class="nx">C</span><span class="o">/</span><span class="nx">C</span><span class="o">++</span> <span class="nx">Header</span>          <span class="mi">9502</span>      <span class="mi">1333790</span>       <span class="mi">103648</span>       <span class="mi">258964</span>       <span class="mi">971178</span>
 <span class="nx">C</span><span class="o">++</span>                   <span class="mi">4069</span>      <span class="mi">1226459</span>       <span class="mi">125398</span>       <span class="mi">200829</span>       <span class="mi">900232</span>
 <span class="nx">C</span>                     <span class="mi">1378</span>       <span class="mi">524592</span>        <span class="mi">64146</span>        <span class="mi">55125</span>       <span class="mi">405321</span>
 <span class="nx">JSON</span>                   <span class="mi">384</span>        <span class="mi">56817</span>            <span class="mi">5</span>            <span class="mi">0</span>        <span class="mi">56812</span>
 <span class="nx">Java</span>                   <span class="mi">399</span>        <span class="mi">71902</span>         <span class="mi">6691</span>        <span class="mi">27203</span>        <span class="mi">38008</span>
 <span class="nx">Python</span>                 <span class="mi">159</span>        <span class="mi">40158</span>         <span class="mi">5446</span>         <span class="mi">5885</span>        <span class="mi">28827</span>
 <span class="nx">Markdown</span>               <span class="mi">286</span>        <span class="mi">34809</span>         <span class="mi">7845</span>            <span class="mi">0</span>        <span class="mi">26964</span>
 <span class="nx">JavaScript</span>             <span class="mi">672</span>        <span class="mi">41390</span>         <span class="mi">2147</span>        <span class="mi">14136</span>        <span class="mi">25107</span>
 <span class="nx">CSS</span>                    <span class="mi">454</span>        <span class="mi">17078</span>         <span class="mi">1295</span>         <span class="mi">6106</span>         <span class="mi">9677</span>
 <span class="nx">Makefile</span>               <span class="mi">167</span>         <span class="mi">8548</span>         <span class="mi">1232</span>         <span class="mi">2302</span>         <span class="mi">5014</span>
 <span class="nx">TypeScript</span>             <span class="mi">126</span>        <span class="mi">19856</span>         <span class="mi">1833</span>        <span class="mi">13331</span>         <span class="mi">4692</span>
 <span class="nx">Plain</span> <span class="nx">Text</span>             <span class="mi">116</span>         <span class="mi">3523</span>          <span class="mi">213</span>            <span class="mi">0</span>         <span class="mi">3310</span>
 <span class="nx">Bourne</span> <span class="nx">Shell</span>            <span class="mi">36</span>         <span class="mi">3755</span>          <span class="mi">432</span>          <span class="mi">657</span>         <span class="mi">2666</span>
 <span class="nx">XML</span>                     <span class="mi">91</span>         <span class="mi">5051</span>          <span class="mi">407</span>         <span class="mi">2108</span>         <span class="mi">2536</span>
 <span class="nx">INI</span>                     <span class="mi">12</span>         <span class="mi">2010</span>           <span class="mi">65</span>          <span class="mi">170</span>         <span class="mi">1775</span>
 <span class="nx">Assembly</span>                <span class="mi">14</span>         <span class="mi">1688</span>          <span class="mi">189</span>          <span class="mi">255</span>         <span class="mi">1244</span>
 <span class="nx">Prolog</span>                   <span class="mi">9</span>         <span class="mi">1101</span>           <span class="mi">71</span>            <span class="mi">0</span>         <span class="mi">1030</span>
 <span class="nx">Protobuf</span>                <span class="mi">22</span>         <span class="mi">1404</span>          <span class="mi">155</span>          <span class="mi">320</span>          <span class="mi">929</span>
 <span class="nx">CMake</span>                   <span class="mi">11</span>          <span class="mi">912</span>           <span class="mi">65</span>           <span class="mi">80</span>          <span class="mi">767</span>
 <span class="nx">HTML</span>                     <span class="mi">1</span>          <span class="mi">470</span>           <span class="mi">17</span>           <span class="mi">16</span>          <span class="mi">437</span>
 <span class="nx">Yacc</span>                     <span class="mi">2</span>          <span class="mi">511</span>           <span class="mi">53</span>           <span class="mi">31</span>          <span class="mi">427</span>
 <span class="nx">Batch</span>                    <span class="mi">8</span>          <span class="mi">508</span>          <span class="mi">110</span>            <span class="mi">0</span>          <span class="mi">398</span>
 <span class="nx">LinkerScript</span>             <span class="mi">4</span>          <span class="mi">168</span>           <span class="mi">18</span>           <span class="mi">44</span>          <span class="mi">106</span>
 <span class="nx">SQL</span>                      <span class="mi">1</span>           <span class="mi">68</span>            <span class="mi">3</span>           <span class="mi">14</span>           <span class="mi">51</span>
 <span class="nx">Autoconf</span>                 <span class="mi">1</span>           <span class="mi">35</span>            <span class="mi">4</span>           <span class="mi">22</span>            <span class="mi">9</span>
<span class="o">--------------------------------------------------------------------------------</span>
 <span class="nx">Total</span>                <span class="mi">17924</span>      <span class="mi">3396603</span>       <span class="mi">321488</span>       <span class="mi">587598</span>      <span class="mi">2487517</span>
<span class="o">--------------------------------------------------------------------------------</span>
</span></code></pre></div><p>相比 1.0，C/C++ 代码新增了大概 2 百万行。JS 新增 3 万行。</p><p>作为一名前端开发者，我重点看了 <code><ROOT>/foundation/ace/ace_engine_lite/</code> 的代码，以及 <code><ROOT>/interface/sdk-js/</code> 的代码。 其他代码在慢慢啃。ace_engine_lite 我一直关注，也给 ace_engine_lite 修复过一些 bug，整体而言，这个模块改动不大。interface/sdk-js 应该是 2.0 新增的，在 1.0 的代码库里面没有。</p><p>从目前源码来看（可能不准确，我的猜测），OpenHarmony 应该是介于硬件和 Android 之间的，封装了几个系统内核，如 linux、liteos_a、liteos_m、……等。而 HarmonyOS 大概率使用了 AOSP（Android Open Source Project）的开源代码。</p>  
</div>
            