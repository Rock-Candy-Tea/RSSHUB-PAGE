
---
title: 'GoLand 2021.3 Beta 2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-77ecf721826fb5b3a599a5f3d80f7481195.png'
author: 开源中国
comments: false
date: Tue, 16 Nov 2021 07:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-77ecf721826fb5b3a599a5f3d80f7481195.png'
---

<div>   
<div class="content">
                                                                                            <p>GoLand 2021.3 Beta 2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fgo%2F2021%2F11%2F12%2Fgoland-2021-3-beta-2-improved-error-messages-for-debugging-tests-and-the-ability-to-compare-profiler-snapshots%2F" target="_blank">已发布</a>，此版本改进了 Debugging Tests 的错误信息和比较分析器快照 (Compare Profiler Snapshots) 的能力。</p> 
<p><strong>改进 Debugging Tests 的错误消息</strong></p> 
<p>当我们在项目树中选择一个目录并运行 Debug | go test 'directoryName'，会得到一个模糊的错误消息。</p> 
<p>发生这种情况是因为，在这种情况下，GoLand 创建了一个带有 Test Kind: Directory 的配置，而我们不能在目录类型的配置中调试测试。</p> 
<p>对于此类错误，显示的信息不是很好理解。</p> 
<p>此版本对这种情况进行了优化，现在错误会提示你不能在目录类型的运行配置中调试测试，但可以对每个包的测试进行调试。</p> 
<p>此外还有一个指向 Run/Debug Configurations 设置的链接，可以在这里将 Test kind 从 Directory 更改为 Package。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-77ecf721826fb5b3a599a5f3d80f7481195.png" referrerpolicy="no-referrer"></p> 
<p><strong><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>可视化分析器快照之间的差异 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>分析器是 GoLand 用于诊断性能问题和探索运行时程序运行的主要工具。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本引入了可视化展示火焰图上两个快照之间差异的功能。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>从打开的项目转到</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:#ffffff; color:#27282c"><span> </span></span><em>Run</em><span style="background-color:#ffffff; color:#27282c"><span> </span>|<span> </span></span><em>Open Profiler Snapshots</em><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><em>。</em>或者按 ⇧ ( <em>Shift</em> )<em> </em>两次，然后在搜索栏中输入</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:#ffffff; color:#27282c">“Open Profiler Snapshots”，</span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>将会看到快照列表。打开其中一个，然后通过重复相同的操作以打开另一个。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>然后单击位于其中一个快照选项卡中的"</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><em>Compare With Baseline</em><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>"按钮。从菜单中，选择要与它比较的快照。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span>Goland 会提供一个单独的差异选项卡来显示比较结果，结合两个火焰图并将差异显示为红色和绿色。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>如果您看到 6% 的帧为绿色，则表示相应方法在第二次分析器运行期间速度提高了 6%。红色表示相应的方法变慢了。  </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1116/075717_GxoK_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fgo%2F2021%2F11%2F12%2Fgoland-2021-3-beta-2-improved-error-messages-for-debugging-tests-and-the-ability-to-compare-profiler-snapshots%2F" target="_blank">完整更新说明查看发布公告</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fgo%2Fnextversion" target="_blank">https://www.jetbrains.com/go/nextversion</a></p>
                                        </div>
                                      
</div>
            