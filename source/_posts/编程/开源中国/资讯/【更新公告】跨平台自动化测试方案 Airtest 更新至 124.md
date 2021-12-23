
---
title: '【更新公告】跨平台自动化测试方案 Airtest 更新至 1.2.4'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1223/150844_IN92_5430600.png'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 07:11:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1223/150844_IN92_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>本次更新为 Airtest 更新，版本提升至 1.2.4 版本。</p> 
<p>PS：AirtestIDE 暂未更新 ，1.2.12版本的 IDE 自带的 Airtest 版本仍是 1.2.3 版本，不是最新的 1.2.4 版本。</p> 
<h2><strong>更新详情</strong></h2> 
<p><strong><span>1）新增对Android12的支持</span></strong></p> 
<p><span>新增Android 12的minicap截图支持。</span></p> 
<p><span>如果在1.2.12版本的IDE中，连接不上Android12的设备，可以在本地python环境把Airtest更到1.2.4版本后，连接Android12的设备跑一个脚本之后，再用1.2.12版本的IDE来连接该设备。（当然，后续更新了AirtestIDE的版本之后，就可以直接连接，无需进行这些操作）</span></p> 
<p><strong><span>2）修复了1个启动录屏失败的问题</span></strong></p> 
<p><span>安卓在录屏强制中止的情况下，下一次启动录屏时优先清理之前的录屏再开始新录屏，有效避免了<span> </span></span><span style="color:#ff0000"><strong>启动录屏失败</strong></span><span><span> </span>的问题。</span></p> 
<p><span>旧版本在录屏强制终止的情况下，重新开始录屏可能会出现如下的报错（需要手动结束录屏或者单独运行结束录屏的脚本之后才能正常重新开启录屏）：</span></p> 
<p><img alt height="115" src="https://static.oschina.net/uploads/space/2021/1223/150844_IN92_5430600.png" width="660" referrerpolicy="no-referrer"></p> 
<p><strong><span>3）优化了部分手机的输入问题</span></strong></p> 
<p><span>部分手机如oppo/vivo等，在没有安装/启用yosemite输入法时无法使用，改用 </span><code><span>adb shell input text</span></code><span> 输入（<span>不支持中文</span>）。</span></p> 
<p><strong><span>4）优化了 </span><code><span>wake</span></code><span> 接口解锁操作</span></strong></p> 
<p><code><span>wake</span></code><span> 接口先尝试使用 </span><code><span>keyevent224</span></code><span> 和 </span><code><span>82</span></code><span> 解锁android屏幕，如果解锁失败，再尝试用yosemite解锁。</span></p> 
<p><strong><span>5）修复了部分极限情况的图像识别异常问题</span></strong></p> 
<p><span>计算置信度过程加入极限值噪点，修复纯色状态时<span> </span></span><span style="color:#ff0000"><strong>置信度异常高</strong></span><span><span> </span>的问题。RGB模式对极限值进行裁剪，修复色相角度计算异常的问题。</span></p> 
<h2>如何更新</h2> 
<p><strong><span>1）使用了AirtestIDE</span></strong></p> 
<p><span>因为本次更新只涉及Airtest框架更新，所以我们即使使用最新的1.2.12版本IDE自带的Python环境也是无法享受到的；</span></p> 
<p><span>但是我们可以在AirtestIDE设置使用本地Python环境，然后在本地Python环境中将 Airtest 更新至1.2.4版本，这样在IDE运行脚本时，就会使用最新的Airtest框架。</span></p> 
<p><strong><span>2）使用本地Python环境/其它编辑器</span></strong></p> 
<p><span>使用本地Python环境同学，可以直接在对应的Python环境中，使用下述命令更新 Airtest：</span></p> 
<pre><code>pip install -U airtest</code></pre> 
<p><span>使用其它编辑器，比如pycharm的同学，可以直接找到当前项目使用的Python解释器，然后升级 Airtest 至1.2.4版本：</span></p> 
<p><img alt height="187" src="https://static.oschina.net/uploads/space/2021/1223/150933_pQDH_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>更新注意事项</h2> 
<p><strong><span>1）pip install 超时/报错</span></strong></p> 
<p><span>如果在下载/更新airtest库时，出现超时问题，请 </span><span style="color:#ff0000"><strong>更换国内源 </strong></span><span>来pip，比如使用清华源：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start"> </pre> 
<p><code><span>pip install -U airtest -<strong>i</strong> https:<em>//pypi.tuna.tsinghua.edu.cn/simple</em></span></code></p> 
<p><span>如果出现报错，不能安装，则优先排查python版本的支持问题，airtest支持3≤python≤3.9。（python2不支持）</span></p> 
<p><strong><span>2）更新后numpy报错</span></strong></p> 
<p><span>如更新后出现类似 </span><code><span>ImportError:numpy.core.multiarray failed to import</span></code><span> 的报错，可以尝试将 </span><code><span>numpy</span></code><span> 库的版本降至1.19.3版本以下：</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start"> </pre> 
<p><code><span><em># 安装指定版本的库（命令参考）</em><br> pip install <span style="color:#000080">numpy</span>==1.17.2</span></code></p> 
<p><span>如果python环境里面的numpy版本＞1.9.13，安装时会出现类似 </span><code><span>airtest 1.2.4 requires numpy≤1.19.3</span></code><span>。请先将环境里面的numpy版本降低至要求以下，再来安装最新的airtest。</span></p> 
<p><strong><span>3）其它关于1.2.4版本Airtest的问题</span></strong></p> 
<p><span>如同学们在使用新版的Airtest时遇到了一些问题无法解决，可以通过此网站向我们的开发者快速提单：</span><span>https://airtest.netease.com/issue_create</span><span> 。</span></p> 
<p><span>可以在标题中加入“Airtest1.2.4”之类的字眼，方便我们快速筛选和排查。</span></p>
                                        </div>
                                      
</div>
            