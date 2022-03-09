
---
title: 'Firefox 98 发布，大幅优化下载功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0309/072817_kNgR_4937141.png'
author: 开源中国
comments: false
date: Wed, 09 Mar 2022 07:29:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0309/072817_kNgR_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Firefox 98 如期而至，该版本最大的变化就是优化了下载流程，除此之外还有一系列的小改进、性能优化和安全性增强。</p> 
<p>Firefox 98 优化了下载流程，改变了浏览器长期存在的一个行为。以往当用户使用 Firefox 下载文件时，浏览器会弹出一个窗口提示，要求用户选择一个开启文件的应用程序，或将文件直接保存到本地（无论如何都要二选一）。从 Firefox 98 开始，所有文件将自动保存到默认的下载文件夹中，不会再弹窗提示了。</p> 
<p><img alt height="217" src="https://static.oschina.net/uploads/space/2022/0309/072817_kNgR_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>除此之外，新版本中还为<strong>下载面板</strong>新增了多个有用的选项（上图）：</p> 
<ul> 
 <li>自动打开该类型文件：让 Firefox 浏览器自动用系统默认的应用程序打开相同类型的下载文件</li> 
 <li>在访达（macOS）或文件夹（Windows）中显示：打开包含下载文件的文件夹</li> 
 <li>转至下载页面：即使在离开网站或关闭标签页面后，也会重新打开最初的下载页面</li> 
 <li>复制下载链接：复制下载链接以分享或保存等用途</li> 
 <li>删除：你现在可以直接从下载面板中删除已下载的文件（不是删除下载记录，而是从设备中彻底删除这个文件，无需跳转至对应的文件夹再进行删除操作）</li> 
 <li>从历史记录中移除：从下载文件列表中删除这个文件的下载记录（仅删除记录，不删除文件）</li> 
 <li>清空预览面板：清空面板中的下载项目列表</li> 
</ul> 
<p>现在用户还可以在文件下载完成<strong>之前</strong>就双击文件，Firefox 会在文件完成后自动开启它。</p> 
<h3>搜索引擎</h3> 
<p>Firefox 浏览器允许用户从一些内置的搜索引擎中选择一个作为默认的搜索引擎。在这个版本中，一些以前配置过默认引擎的用户会注意到他们的默认搜索引擎已经发生了改变，因为 Mozilla 无法获得部分搜索引擎提供商的正式许可，因此需要移除部分搜索引擎，<strong>中国大陆用户并未发生任何变化</strong>（<a href="https://www.oschina.net/news/183106/search-engine-removal">可查看我们这篇报道</a>）。</p> 
<h3>其他内容：</h3> 
<ul> 
 <li>更新到 Firefox 98 后，“总是询问” 下载操作现在将被重置；</li> 
 <li>在 Firefox 98 的 Linux 版本中，Wayland 支持默认并没有启用。有需要的用户可以手动启用 Wayland 支持；</li> 
 <li>这个版本将通过只使用 webRequest 阻塞调用来改善启动期间加载附加组件的情况，此前 webRequest 非阻塞调用会导致附加组件提前启动，这会引发 Firefox 出现性能问题，现在 Firefox 浏览器的启动速度将变得更快；</li> 
 <li>Firefox 98 默认启用了 <dialog> HTML 元素，以增加对基于 HTML 的模态对话框的支持；</li> 
 <li>增加了对 HTMLElement.outerText DOM 元素的支持；</li> 
 <li>改进了 navigator.registerProtocolHandler() API；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mozilla.org%2Fen-US%2Ffirefox%2F98.0%2Freleasenotes" target="_blank">https://www.mozilla.org/en-US/firefox/98.0/releasenotes</a></p>
                                        </div>
                                      
</div>
            