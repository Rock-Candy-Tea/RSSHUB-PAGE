
---
title: 'Win11的TPM再次被蹂躏 U盘工具Ventoy也能破解了'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211019/73f80c0d-e936-4159-84ae-b87ee4eeee34.jpg'
author: 快科技（原驱动之家）
comments: false
date: Tue, 19 Oct 2021 20:57:53 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211019/73f80c0d-e936-4159-84ae-b87ee4eeee34.jpg'
---

<div>   
<p>在Win11系统上，微软在硬件要求上加入了一个理由足够强但大家都不喜欢的门槛，那就是必须要支持TPM安全防护，还是TPM 2.0版的。这会导致很多旧机无法升级，不过现在TPM的要求也是名存实亡了，U盘工具Ventoy最新版也能破解TPM了。</p>
<p>我们之前提到过很多绕过TPM限制的软件，除了网上流传的注册表修改之外，<a class="f14_link" href="https://news.mydrivers.com/1/788/788280.htm" target="_blank">通过WinPE、Rufus等装机工具也可以</a>，现在的Ventoy 1.0.55也有类似的效果，这也是一个很出名的U盘工具。</p>
<p>使用Ventoy 1.0.55绕过TPM的过程也很简单，下载之后解压，然后在Ventoy 1.0.55的安装子目录中新建新的文本文档并将其命名为 ventoy.json。</p>
<p>接着在这个json文件中写入以下代码并保存：</p>
<p><em>&#123;</em></p>
<p><em>“control”: [</em></p>
<p><em>&#123; “VTOY_DEFAULT_MENU_MODE”: “0” &#125;,</em></p>
<p><em>&#123; “VTOY_TREE_VIEW_MENU_STYLE”: “0” &#125;,</em></p>
<p><em>&#123; “VTOY_FILT_DOT_UNDERSCORE_FILE”: “1” &#125;,</em></p>
<p><em>&#123; “VTOY_SORT_CASE_SENSITIVE”: “0” &#125;,</em></p>
<p><em>&#123; “VTOY_MAX_SEARCH_LEVEL”: “max” &#125;,</em></p>
<p><em>&#123; “VTOY_DEFAULT_SEARCH_ROOT”: “/ISO” &#125;,</em></p>
<p><em>&#123; “VTOY_MENU_TIMEOUT”: “10” &#125;,</em></p>
<p><em>&#123; “VTOY_DEFAULT_IMAGE”: “/ISO/debian_netinstall.iso” &#125;,</em></p>
<p><em>&#123; “VTOY_FILE_FLT_EFI”: “1” &#125;,</em></p>
<p><em>&#123; “VTOY_DEFAULT_KBD_LAYOUT”: “QWERTY_USA” &#125;,</em></p>
<p><em>&#123; “VTOY_WIN11_BYPASS_CHECK”: “1” &#125;</em></p>
<p><em>]</em></p>
<p><em>&#125;</em></p>
<p><span style="color:#ff0000;"><strong>这样操作之后，Ventoy 1.0.55也可以绕过Win11安装的TPM、安全启动、4GB内存、CPU及硬盘等限制了，破解的限制很多，适合旧机器升级。</strong></span></p>
<p>Ventoy 1.0.55下载页面：<a class="f14_link" href="https://github.com/ventoy/Ventoy/releases" target="_blank">点此进入</a>（网上还有很多分流下载）</p>
<p style="text-align: center"><img alt="Win11的TPM再次被蹂躏 U盘工具Ventoy也能破解了" h="400" src="https://img1.mydrivers.com/img/20211019/73f80c0d-e936-4159-84ae-b87ee4eeee34.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a></p>
<p class="url">
     
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            