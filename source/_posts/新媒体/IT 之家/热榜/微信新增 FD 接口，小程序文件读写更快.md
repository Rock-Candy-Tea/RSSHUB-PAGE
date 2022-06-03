
---
title: '微信新增 FD 接口，小程序文件读写更快'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/6/56e256fb-80b6-473d-8a88-b21dc94081e0.png'
author: IT 之家
comments: false
date: Thu, 02 Jun 2022 04:52:52 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/6/56e256fb-80b6-473d-8a88-b21dc94081e0.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1702727" rel="nofollow">菜菜狗</a> 的线索投递！</div>
            <p data-vmark="b2ee"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 6 月 2 日消息，文件操作太麻烦？文件读写速度太慢？……</p><p data-vmark="a1b6">据<a href="https://mp.weixin.qq.com/s/tgniUyCL9BktNMQYzddhHg" target="_blank">微信开发者</a>发布，随着文件系统本地存储容量的不断扩大，文件操作的流程与速度成为开发者们日益关注的重点。为了实现小程序 / 小游戏更高效、更原子化的文件操作效果，微信团队新增 FD 接口，优化小程序用户体验：</p><ul class=" list-paddingleft-2"><li><p data-vmark="92af">支持一次打开文件即可多次读 / 写，减少重复操作</p></li><li><p data-vmark="8fb8">支持只读 / 写指定内容，减少无效读写</p></li><li><p data-vmark="82d6">实现读写耗时降低 46%，提升体验</p></li></ul><p data-vmark="b15e"><img src="https://img.ithome.com/newsuploadfiles/2022/6/56e256fb-80b6-473d-8a88-b21dc94081e0.png" w="942" h="2672" title="微信新增 FD 接口，小程序文件读写更快" width="942" height="2326" referrerpolicy="no-referrer"></p><h3 data-vmark="03ec">FD 接口是什么</h3><p data-vmark="2e44"><span class="accentTextColor">FD 接口是微信团队新增的高性能、原子化的文件接口类型。</span>对比原有文件接口，FD 接口不仅增加打开文件与关闭文件 2 个接口，而且更新代码实现方式，快速提升小程序性能。</p><h3 data-vmark="41aa">FD 接口有多强</h3><p data-vmark="ad6a">FD 接口支持一次打开文件，即可进行多次读 / 写操作。对比原有文件接口每项操作均需要打开、写入、关闭文件 3 个步骤，FD 接口实现一次打开文件，即可多次读取、写入文件，操作完成再关闭文件，减少重复操作。</p><p data-vmark="c309">FD 接口支持只读 / 写文件中指定内容。针对大文件操作场景，FD 接口的该项特性能够减少无效读写，降低文件读写时间。 如下图例子，原有文件接口需要全部读 / 写内容（如左下图黄色高亮内容），FD 文件接口则支持只读 / 写指定内容（如右下图黄色高亮内容），降低读写耗时。</p><p data-vmark="7972">以连续 100 次读 + 写同一个文件 (1MB) 的实验为例，对比原有接口读写文件耗时，FD 接口在安卓端读写文件耗时降低 46%，在 iOS 端读写耗时降低 19%。</p><h3 data-vmark="fb70">FD 接口怎样用</h3><p data-vmark="5556">FD 接口减少重复操作、减少无效读写，降低文件读写耗时。那么如何正确应用 FD 接口？</p><p data-vmark="3f91">以打开文件、读取文件内容、修改内容并写入文件的过程为例，原有接口需要每次读写文件并且完整打开关闭。</p><pre>// 获取全局唯一的文件管理器
const fs = wx.getFileSystemManager()
// 读取文件
data = fs.readFileSync(“FileA”)
// 修改文件内容
data = modify(data)
// 写入文件
fs.writeFileSync(“FileA”, data)</pre><p data-vmark="7387">如果仅应用于简单的文件操作流程，原有文件接口仍可适用。但面向大量文件操作的场景，原有文件接口造成读写耗时较长，同时影响低端机型的性能，影响用户体验。因此 FD 接口一次打开、多次执行的特性能够高效解决问题，代码示例如下：</p><pre>// 获取全局唯一的文件管理器
const fs = wx.getFileSystemManager()
// 打开文件
fd = fs.openSync(“FileA”)
// 读取文件
fs.readSync(&#123; fd, arrayBuffer, offset, length, position &#125;)
// 修改文件内容
data = modify(data)
// 写入文件
fs.writeSync(&#123; fd, data, offset, length, position &#125;)
// 关闭文件
fs.closeSync(&#123;fd: fd &#125;)</pre><p data-vmark="0136">面对文件系统本地存储容量的不断扩大的场景，FD 接口支持一次打开文件即可多次读 / 写，并且支持只读 / 写指定内容，实现文件读写耗时减少近 50%，提升用户体验。</p><p data-vmark="d392">大家在<a href="https://wxaurl.cn/tIhrCxgH5Kb" target="_blank" data-androidurl="ithome://openmp?appid=ithome&path=pages%2Fwebview%2Fwebview%3Furl%3Ditmp" data-iosurl="ithome://openmp?appid=ithome&path=pages%2Fwebview%2Fwebview%3Furl%3Ditmp" data-wxmpurl="ithome://openmp?appid=ithome&path=pages%2Fwebview%2Fwebview%3Furl%3Ditmp" data-wapurl="https://wxaurl.cn/tIhrCxgH5Kb">IT之家微信号</a>回复“<span class="font-color-red">微信</span>”两字，即可获取当前最新官方内部版微信下载。</p><p data-vmark="fa2a" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2021/3/20210316222136_9513.jpg" alt title="微信新增 FD 接口，小程序文件读写更快" referrerpolicy="no-referrer"> </p><p data-vmark="f57f" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/0c06136f-d56c-4f12-806e-e322619f78c2.png" w="1440" h="799" title="微信新增 FD 接口，小程序文件读写更快" width="1440" height="455" referrerpolicy="no-referrer"> </p>
          
</div>
            