
---
title: '想尝鲜Win11？虚拟机安装Windows 11详细教程'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211018/S362fc52e-72a1-423e-a779-b33512aa75f4.png'
author: 快科技（原驱动之家）
comments: false
date: Mon, 18 Oct 2021 22:38:13 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211018/S362fc52e-72a1-423e-a779-b33512aa75f4.png'
---

<div>   
<p>]Windows 11正式版来了，想要先体验一下看看是不是自己的菜，才决定是否用它替换旧系统，那用VMware Workstation虚拟机来体验一下，这是个不错的方法。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211018/362fc52e-72a1-423e-a779-b33512aa75f4.png" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="432" src="https://img1.mydrivers.com/img/20211018/S362fc52e-72a1-423e-a779-b33512aa75f4.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图1 VMware Workstation</p>
<p>可是目前在VMware Workstation（后简称VM）中安装会遇到“此电脑无法运行Windows 11”的错误提示，怎么回事呢？</p>
<p>那是因为用户把虚拟机的内存配置的太低，也没有给虚拟机加密，更没有添加上TPM虚拟硬件，所以无法直接安装Windows 11了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211018/e362f2f8-3b22-49c4-8acb-fdae129eb950.png" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="450" src="https://img1.mydrivers.com/img/20211018/Se362f2f8-3b22-49c4-8acb-fdae129eb950.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图2 虚拟机安装Windows 11 出错</p>
<p>没事，跟着小编来，一步一步创建一个可以正常安装Windows 11的虚拟机环境。新手按照教程一步一步来，很快就能创建一个虚拟机，而想看怎么设置才能安装Windows 11的老鸟们往下翻跳过创建虚拟机步骤即可。</p>
<p><strong>VMware Workstation安装Windows 11 具体步骤。</strong></p>
<p><strong>步骤一 创建虚拟机</strong></p>
<p>要使用VM来体验Windows 11，首先要做的就是在VM里创建一个虚拟机，具体的创建虚拟机步骤，你只需要跟着下边的图一步一步走就好，只需要留意一下，内存设置需要大于4G。</p>
<p>至于如何下载Windows 11官方安装镜像文件，可以参考小编的另一篇文章。链接在这里：https://pcedu.pconline.com.cn/1461/14619444.html</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/3e687769-e178-447e-b3c8-675328325f16.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图3 新建虚拟机</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/12c74406-270a-4287-b786-3136fdb56dcb.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图4 下一步</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/e7453665-c3c2-4f15-a21a-98727dd264d8.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图5 选择安装程序光盘，加载Windows 11安装镜像文件</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/e0cb3995-799e-4889-8cbb-fe43235b0b40.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图6 默认即可，选Windows 10 X64</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/6a3fc74a-a874-4c05-b0a4-249c8babe59d.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图7 选择虚拟机保存位置</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/81b15736-cde5-4117-8d8e-ed1e310bfa97.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图8 选择UEFI勾选安全引导</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/2fa9e326-7e42-4911-a731-db7d81788fc6.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图9 2/2 即可</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/4df9fe39-4c9c-479e-bfa7-d167caaeef12.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图10 必须大于4G内存</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/ef019acc-d138-446e-a936-831454cc7dc5.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图11 使用桥接网络或网络地址转换都可</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/10b1be60-610d-4d3d-aa90-4340db46f769.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图12 推荐即可</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/b09e92eb-30fb-452d-a26e-95ce300b76dc.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图13 推荐即可</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/a4a74739-4fdb-46a4-a5ef-5e8c5d1ce0af.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图14 创建新虚拟磁盘</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/f63e4d43-1711-4c53-b0aa-cceed26bccad.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图15 设置新虚拟磁盘大小</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/ecc9d308-2d3f-4c8e-97d0-d55b4a286b97.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图16 选择虚拟磁盘文件保存位置</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="433" src="https://img1.mydrivers.com/img/20211018/4dcea282-b95a-4ab8-bc55-6119c426a82b.png" style="border: black 1px solid" w="499" referrerpolicy="no-referrer"><br>
图17 完成虚拟机创建</p>
<p>到此，一个新的虚拟机创建完毕，如果是安装Windows 10的话，直接开启虚拟机然后安装系统即可，但是安装Windows 11的话，还需要进行以下设置。</p>
<p><strong>步骤二 设置可安装运行Windows 11的虚拟机环境</strong></p>
<p>接下来我们就得为刚刚创建的虚拟机进行设置，以便让它能够安装运行Windows 11。这里我们需要把虚拟机进行加密及添加虚拟TPM安全芯片。</p>
<p>加密虚拟机步骤：选择刚刚创建的的虚拟机，右键菜单→设置→选项→访问控制→加密→设置密码→加密。</p>
<p style="text-align: center"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="505" src="https://img1.mydrivers.com/img/20211018/35ee5cb3-2607-4291-b712-7774e8741f7e.png" style="border: black 1px solid" w="422" referrerpolicy="no-referrer"><br>
图18 虚拟机设置</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211018/b89eca44-eab1-4add-9eb8-70df0255440b.png" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="656" src="https://img1.mydrivers.com/img/20211018/Sb89eca44-eab1-4add-9eb8-70df0255440b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图19 访问控制</p>
<p>添加虚拟TPM安全芯片步骤：虚拟机设置→硬件→添加→添加可信平台模块。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211018/ccdf6aca-601e-4be2-9dee-366bf219efa6.png" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="654" src="https://img1.mydrivers.com/img/20211018/Sccdf6aca-601e-4be2-9dee-366bf219efa6.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图20 添加新硬件</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211018/ba357ae0-fbc9-4e1a-bc46-0fb361009ad2.png" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="654" src="https://img1.mydrivers.com/img/20211018/Sba357ae0-fbc9-4e1a-bc46-0fb361009ad2.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图21 添加可信平台模块</p>
<p><strong>步骤三 正常安装Windows 11</strong></p>
<p>设置完毕后，就是开启虚拟机，按照正常的步骤安装Windows 11即可。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211018/2259d1f1-3e1d-491c-916f-214b6289498b.png" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="432" src="https://img1.mydrivers.com/img/20211018/S2259d1f1-3e1d-491c-916f-214b6289498b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图22 正常安装Windows 11</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211018/d59d8a98-552b-450e-9f04-d2dc6068f542.png" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="432" src="https://img1.mydrivers.com/img/20211018/Sd59d8a98-552b-450e-9f04-d2dc6068f542.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图23 正常安装Windows 11</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211018/bb92d981-7b54-4eac-9241-54556b6cfeee.png" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="432" src="https://img1.mydrivers.com/img/20211018/Sbb92d981-7b54-4eac-9241-54556b6cfeee.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
图24 正常安装Windows 11</p>
<p><strong>总结</strong></p>
<p>怎么样，你用VM体验上Windows 11了没。虽然Windows 11用起来跟Windows 10没多大区别，但是一些不一样的操作步骤还是需要时间去适应的，先体验一下再来做决定会是个不错的决定哦。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211018/37c50b7e5c1c4940877cfe9876c0dde3.jpg" target="_blank"><img alt="想尝鲜Win11？虚拟机安装Windows 11详细教程" h="400" src="https://img1.mydrivers.com/img/20211018/s_37c50b7e5c1c4940877cfe9876c0dde3.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win11/1462/14622624.html">太平洋电脑网</a></span>
<span>责任编辑：陈驰</span>
</p>
        
</div>
            