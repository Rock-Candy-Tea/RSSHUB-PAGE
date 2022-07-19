
---
title: '笔记本 CPU 莫名锁频率 0.39GHz？教你解决这个 Bug'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/7/a02b3e9b-6b09-495e-a947-387f8609ff8d.jpg'
author: IT 之家
comments: false
date: Mon, 18 Jul 2022 07:28:47 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/7/a02b3e9b-6b09-495e-a947-387f8609ff8d.jpg'
---

<div>   
<p data-vmark="10b0">夏天来了，一些奇奇怪怪的软硬件问题又开始出现了。近日，有朋友向笔者反馈，说笔记本从休眠模式恢复后，<span class="accentTextColor">CPU 频率被锁定在 0.39GHz</span>，无论插电与否都停留在这个频率，导致系统卡顿无比！这到底要如何解决？其实和 Windows 的电源策略有关。</p><p data-vmark="a695" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/7/a02b3e9b-6b09-495e-a947-387f8609ff8d.jpg" w="700" h="588" alt="CPU锁0.39 CPU锁0.78" title="笔记本 CPU 莫名锁频率 0.39GHz？教你解决这个 Bug" width="700" height="588" referrerpolicy="no-referrer"></p><p data-vmark="aff5">当检测到电池电量不足的时候，Windows 系统会强制关机。但于此同时，Windows 还会抢先在关机前，将当前的内存数据写入硬盘，以方便下次开机的时候恢复，无需丢失工作进度。实则上，系统进入的是休眠状态，而不是完全的关机。</p><p data-vmark="7191">而在将数据写入硬盘时，为了防止突然掉电导致写入失败，此时系统可能会将 CPU 频率控制在比较低的频率，减少能耗，保证完成数据写入的过程。</p><p data-vmark="3cb8">另外，<span class="accentTextColor">在笔记本发热过大的时候，也可能会触发 CPU 强制降频</span>，将 CPU 频率锁定到较低频率，这个频率比较常见的是 0.39GHz 或者 0.78GHz。触发 CPU 降频后，系统也可能会强制休眠，将内存数据写入到硬盘后进入休眠状态。</p><p data-vmark="587b" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/7/84f4415e-c616-4879-9186-32758db67cbc.jpg" w="700" h="350" alt="CPU%u95010.39%20CPU%u95010.78" title="笔记本 CPU 莫名锁频率 0.39GHz？教你解决这个 Bug" width="700" height="350" referrerpolicy="no-referrer"></p><p data-vmark="b3c6">Win10 和 Win11 都有类似的机制。然而问题就来了，这个 CPU 降频后进入休眠状态的机制可能存在 Bug，当电脑从休眠恢复过来的时候，CPU 频率可能不会恢复，依然保持在 0.39GHz 之类的低频！这就导致了文章开头所说 CPU 频率被锁定在 0.39GHz 的情况，整个系统都缓慢卡顿，无法正常使用。这种情况，连重启电脑可能也无法解决，因为重启属于热启动，不会检测硬件并重新加载数据，如果 Win10 和 Win11 保存了一些关机前的状态数据，很有可能连 CPU 的锁频状态也会在重启后继续维持。</p><p data-vmark="e491">要如何解决这个问题？这里提供两种可供尝试的解决方法。</p><h2 data-vmark="fddd">长按电源键强制关机再启动</h2><p data-vmark="bf27">系统恢复时带上了休眠前的状态数据，这可能是 CPU 锁频的诱因。如果出现了锁频，我们可以通过<span class="accentTextColor">长按电源键强制关机</span>来尝试解决。</p><p data-vmark="2ff1">长按电源键强制关机，电脑将不会保存关机前的任何数据，也会清理掉一些和系统状态相关的设置。当再次开机的时候，电脑属于冷启动，CPU 锁频设置被清空，频率也就恢复正常了。</p><h2 data-vmark="8cbc">使用 ThrottleStop 关闭过热保护</h2><p data-vmark="e45f"><strong>ThrottleStop：</strong><a href="https://www.techpowerup.com/download/techpowerup-throttlestop/" target="_blank">点此下载</a></p><p data-vmark="f23c">如果不想重启电脑，那么可以用 ThrottleStop 这款小工具尝试解决。ThrottleStop 是由著名硬件评测网站 TechPowerUp 开发的一款小工具，面向 DIY 玩家，用以监视 CPU 以及设置一些和 CPU 相关的选项。在 ThrottleStop 当中，可以找到 <span class="accentTextColor">BD PROCHOT</span> 这一项，取消勾选，去除 CPU 的过热保护，保存后 CPU 频率可能就恢复正常了。</p><p data-vmark="ec39" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/7/021afafe-1626-49ea-8edc-934575fd9e8e.png" w="543" h="464" alt="CPU锁0.39 CPU锁0.78" title="笔记本 CPU 莫名锁频率 0.39GHz？教你解决这个 Bug" width="543" height="464" referrerpolicy="no-referrer"></p><p data-vmark="12dd">总的来说，这是一个系统进入休眠状态或者过热保护时、CPU 降频所引发的 Bug。如果大家遇到了类似情况，不妨尝试一下本文的方法吧，也希望微软可以尽快修复这个问题！</p>
          
</div>
            