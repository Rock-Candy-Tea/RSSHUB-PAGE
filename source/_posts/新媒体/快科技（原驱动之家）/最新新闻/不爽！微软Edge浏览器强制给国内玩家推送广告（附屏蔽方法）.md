
---
title: '不爽！微软Edge浏览器强制给国内玩家推送广告（附屏蔽方法）'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210824/S76d7512f-3334-49b1-93ba-cab19c3523fa.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 24 Aug 2021 17:59:43 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210824/S76d7512f-3334-49b1-93ba-cab19c3523fa.png'
---

<div>   
<p>微软的Edge浏览器改用Chromium内核如获新生，现在已经成为仅次于Chrome的第二好用浏览器了。然而微软也不是做慈善的，现在开始给Edge浏览器加广告了，国内用户会被强制加载广告。</p>
<p>现在打开Edge浏览器，新标签页会花费一点时间加载出来一些链接，<span style="color:#ff0000;"><strong>微软倒是很诚实地注明了是广告，这是微软根据地区属性推的广告，之前还能关闭，现在无法禁用了，对有洁癖的用户来说这不能忍。</strong></span></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210824/76d7512f-3334-49b1-93ba-cab19c3523fa.png" target="_blank"><img alt="不爽！微软Edge浏览器强制给国内玩家推送广告（附屏蔽方法）" h="137" src="https://img1.mydrivers.com/img/20210824/S76d7512f-3334-49b1-93ba-cab19c3523fa.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>为了屏蔽这些广告，网友分享了两种方法，首先是传统的hosts屏蔽法，<strong>打开系统的hosts文件，目录是C:\Windows\System32\drivers\etc，</strong>然后用文本编辑器加入以下内容：</p>
<p>0.0.0.0 ntp.msn.com</p>
<p>0.0.0.0 ntp.msn.cn</p>
<p>0.0.0.0 assets.msn.cn</p>
<p>0.0.0.0 api.msn.com</p>
<p>0.0.0.0 browser.events.data.msn.com</p>
<p>0.0.0.0 img-s-msn-com.akamaized.net</p>
<p>这样就可以屏蔽微软Edge加载的广告了，而且也不影响Edge浏览器更新。</p>
<p>第二种方法更复杂一点，但不需要改动系统文件，是通过启动策略实现的。</p>
<p>具体来说，<span style="color:#ff0000;"><strong>右键点击微软浏览器图标选择属性，然后在目标结尾追加 --force-local-ntp（注意有个空格）），然后保存设置。</strong></span></p>
<p>如果Edge浏览器放在了任务栏上，可以右键点击任务栏图标、再次右键点击 Edge 然后左键点击属性，添加上面的代码就可以了。</p>
<p style="text-align: center"><img alt="不爽！微软Edge浏览器强制给国内玩家推送广告（附屏蔽方法）" h="658" src="https://img1.mydrivers.com/img/20210824/e6640909-213e-4bf1-bcb5-d6c144521d45.png" style="border:black 1px solid" w="474" referrerpolicy="no-referrer"></p>
<p>屏蔽之后，再新建标签页，广告就没有了，干干净净清清爽爽的Edge回来了。</p>
<p><strong>更新</strong>：微软官方已经确认这个问题，微软 Edge（中国）工程团队已于下午确认问题，正在针对相关问题开展调查和处理工作，Edge 浏览器预计将于24小时内恢复正常。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210824/2c719c20-bca8-4960-b5b4-c8256c2d84eb.png" target="_blank"><img alt="不爽！微软Edge浏览器强制给国内玩家推送广告（附屏蔽方法）" h="360" src="https://img1.mydrivers.com/img/20210824/S2c719c20-bca8-4960-b5b4-c8256c2d84eb.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/guanggao.htm"><i>#</i>广告</a><a href="https://news.mydrivers.com/tag/edgeliulanqi.htm"><i>#</i>Edge浏览器</a></p>
<p class="url">
     
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            