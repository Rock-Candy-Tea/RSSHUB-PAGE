
---
title: 'itest work 接口测试&敏捷测试管理平台 9.5.0 GA_u1，优化及修复关键 BUG'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-967355dacf2f8ccbe9c96c2a37763a32aad.png'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 08:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-967355dacf2f8ccbe9c96c2a37763a32aad.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <p>（一)<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F120.78.0.137%2Fitestmanual%2520.pdf" target="_blank"><strong>itest work 简介</strong></a></p> 
   <p> itest work (爱测试)  一站式工作站让测试变得简单、敏捷,“好用、好看，好敏捷” ,是itest wrok 追求的目标。itest work 包含极简的任务管理，测试管理，缺陷管理，测试环境管理，接口测试，接口Mock，还有压测 ，又有丰富的统计分析，<strong>8合1工作站</strong>。可按测试包分配测试用例执行，也可建测试迭代(含任务，测试包，BUG，接口)来组织测试工作，也有测试环境管理，还有很常用的测试度量；对于发版频繁，需求常变，itest还可导出用例，线下修改、执行，新增后再导入（同步）到线上；且可根据测试策略来设置测试流程，并可实时调整；在测试看板中，能查看迭代报告，测试包执行情况，测试任务进展，也可以在看板上直接执行用包用例，也支持在线web 思维导图写用例。概念及功能模型如下：</p> 
   <p><img height="823" src="https://oscimg.oschina.net/oscnet/up-967355dacf2f8ccbe9c96c2a37763a32aad.png" width="1707" referrerpolicy="no-referrer"></p> 
   <p><img height="831" src="https://oscimg.oschina.net/oscnet/up-069dbefc2e5ac1747a970be6a1dca69e046.png" width="1661" referrerpolicy="no-referrer"></p> 
   <p><strong><strong>官网<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.itest.work" target="_blank">  http://www.itest.work</a></strong></strong></p> 
   <p><strong>在线体验1  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.itest.work%2Fdemo" target="_blank">http://www.itest.work/demo </a></strong></p> 
   <p><strong>在线体验2  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhttp%3A%2F%2F120.78.0.137%2Fdemo" target="_blank">http://120.78.0.137/demo </a></strong></p> 
   <p><strong>v9.5.0  GA _u1下载地址 </strong>：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F120.78.0.137%2Frsf%2Fsite%2Fitest%2Fdownload%2Findex.html" target="_blank">itest下载</a></p> 
   <p><strong>二：9.5.0 GA_u1更新说明</strong></p> 
   <p>9.5.0 <strong>GA</strong>(17个更新)<strong> </strong> 4月2号发布后，带着17个更新且含2个BUG修复的9.5.0  GA_u1 又来了<strong>，用户的持续反馈是我们不断更新的动力!4月底发布新一版源码到开源中国上，当前忙着快速迭代，接口测试和实现压测功能。</strong></p> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.itest.work%2Fitest%2Fversion%2FversionUpdate" target="_blank">查看版本更新历史</a></p> 
   <p><strong>9.5.0  </strong>GA_u1 <strong> 主要增加测试总结归档，体验上的优化及解决接口测试9.5.0 GA一个大BUG。</strong><br> <strong>另外在此也预告一下压测功能延期(计划赶不上变化)到4月22发布。</strong></p> 
   <div>
    <strong><strong>9.5.0 GA_u1 详情如下:</strong></strong>
   </div> 
   <div>
    <strong>15个增强：</strong>
   </div> 
   <div>
    1、脑图执行用例页面对齐。
    <br> 2、开始参加项目，后来不参加项了，他还可以切换进入到项目。
    <br> 3、项目简报下钻时，人员信息不对。
    <br> 4、树图标优化，解决有些分辨率下，显示不清晰。
    <br> 5、产品用例库，可以批量删。
    <br> 6、总结附件优化，且总结分类做优化。
    <br> 7、产品用例库，公共用例库节点上标示用例数。
    <br> 8、总结加操作日志。
    <br> 9、总结架删除权限制控制。
    <br> 10、产品用例库权限细化。
    <br> 11、更新手册中接口测试部分的内容。
    <br> 12、ldap配置更改以更通用。
    <br> 13、任何项目模板都能看到项目总结菜单。
    <br> 14、用例包分配用例时，左则的树，如层级深，加了横向滚动条。
   </div> 
   <div>
    15、更新用户手册中接口测试中部分内容
   </div>   
   <div> 
    <p><strong>2个bug修复:</strong></p> 
    <p>1、解决缺陷管理流程开启分析流程时，有时候提交BUG报错的问题。<br> 2、接口测试解决一个重大bug，认证时好时不好的问题。</p> 
    <p><strong>三：9. X 版本之后新 UI </strong></p> 
    <p>预览新UI</p> 
    <p><img height="826" src="https://oscimg.oschina.net/oscnet/up-3019b7f6b2c3da55bd00abc647b35cbb49f.png" width="1913" referrerpolicy="no-referrer"></p> 
    <p><img height="763" src="https://oscimg.oschina.net/oscnet/up-9779be6130c9ee55721e833e383e8a21862.png" width="1813" referrerpolicy="no-referrer"></p> 
    <p><img height="837" src="https://oscimg.oschina.net/oscnet/up-caab15ea05d58bfe2295e57b82a1ef5fd9f.png" width="1920" referrerpolicy="no-referrer"></p> 
    <p><img height="810" src="https://oscimg.oschina.net/oscnet/up-188229bc1d1c64053cda15dc431d19acd2b.png" width="1432" referrerpolicy="no-referrer"></p> 
    <p> </p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-a85ad686b6e5e3065bb75a0bdba749d1f56.png" referrerpolicy="no-referrer"></p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-ac59c509562a63fd9df18b118537ec1a891.png" referrerpolicy="no-referrer"></p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-bf1b84107a09763fb6b94365dcac5663f03.png" referrerpolicy="no-referrer"></p> 
    <p><img height="822" src="https://oscimg.oschina.net/oscnet/up-579cb04f7c06abc04d6aeb4ea6a12776120.png" width="1601" referrerpolicy="no-referrer"></p> 
    <p><img height="726" src="https://oscimg.oschina.net/oscnet/up-c55e8c96ec29ff5f8dfd4f6bf5b5830510c.png" width="1807" referrerpolicy="no-referrer"></p> 
    <p><strong>四：接口测试及新特性截图</strong></p> 
    <p>  截止9.0.1接口测试，已包含接口mock ,接口加密，解密和签名，接口参数化，接口间动态参数传寄，接口依赖推导，建测试测试场景时，自动加入依赖的接口并按依赖关系排好执行顺序，拖拽生成断言，拖拽提取参数  。</p> 
    <p><strong>脑图用例可以通过ctrl+c 复制分支节点，然后ctrl +v 粘贴到其他脑图文件上，可以是同跨项目间粘贴</strong></p> 
    <p><strong>脑图视图，整个项目全部用例显示在一个脑图上，方便梳理用例间关系</strong></p> 
    <p><img alt src="https://img2020.cnblogs.com/blog/261867/202103/261867-20210304092151973-55351996.png" referrerpolicy="no-referrer"></p> 
    <p> </p> 
    <p> </p> 
    <p>BUG 密度分析加增加kloc bug率及功能点BUG率</p> 
    <p><img height="750" src="https://oscimg.oschina.net/oscnet/up-4e7d2192f5d8f085de2a9bfe33709d4bb37.png" width="1811" referrerpolicy="no-referrer"></p> 
    <p>增加迭代汇总导出,5个sheet ，第一个是汇总，后4个是明细</p> 
    <p><img height="721" src="https://oscimg.oschina.net/oscnet/up-e1c0f6fc95e19b9d3fd5a5be4804b896131.png" width="1380" referrerpolicy="no-referrer"></p> 
    <p>增加项目 BUG用例简报，并可下钻到人</p> 
    <p><img height="808" src="https://oscimg.oschina.net/oscnet/up-5cc95faabaa71f2da9f395db05e3e793fdd.png" width="1913" referrerpolicy="no-referrer"></p> 
    <p><strong><img alt src="https://img2020.cnblogs.com/blog/261867/202102/261867-20210204121539296-988882878.png" referrerpolicy="no-referrer"></strong></p> 
    <p><img alt src="https://img2020.cnblogs.com/blog/261867/202102/261867-20210204122017677-169773991.png" referrerpolicy="no-referrer"></p> 
    <p><img alt src="https://img2020.cnblogs.com/blog/261867/202102/261867-20210204122555376-2103563165.png" referrerpolicy="no-referrer"></p> 
    <p> </p> 
    <p> 为结省时间，不在新UI中 一载图了，直接用老版本U I示意</p> 
    <p><strong><img alt src="https://img2020.cnblogs.com/blog/261867/202012/261867-20201231103037523-394025329.png" referrerpolicy="no-referrer"></strong></p> 
    <p> <img alt src="https://img2020.cnblogs.com/blog/261867/202012/261867-20201231102340381-580157965.png" referrerpolicy="no-referrer"></p> 
    <p>呱唧  1800次混沌测试完成了</p> 
    <p><img alt src="https://img2020.cnblogs.com/blog/261867/202012/261867-20201231102013961-1797488725.png" referrerpolicy="no-referrer"></p> 
    <p><img height="973" src="https://oscimg.oschina.net/oscnet/up-8405f3b40434fc7f28177dd634dfb4fd0e7.png" width="866" referrerpolicy="no-referrer"></p> 
    <p>执行测试场景时，先执行正向用例，如check 混沌开关，正向执行完后执行接口混沌测试</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-3355cfdef8e0244c041ef373594dcc1cd76.png" referrerpolicy="no-referrer"></p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-097964a5accbfb6228338a35f605d905612.png" referrerpolicy="no-referrer"></p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-39d013707dd51816ba5f1278bb758ae823b.png" referrerpolicy="no-referrer"></p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-4ecbd29ad331e3b3080fd829e2bf21dfe32.png" referrerpolicy="no-referrer"></p> 
    <p>接口数据参数化</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-80dd4d626e5aecddb787cb3569147aa49e6.png" referrerpolicy="no-referrer"></p> 
    <p>下面是上图以数化在执行时打印出来的值</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-2c6ddec3eb70a56568e59cfa1b95722b4ec.png" referrerpolicy="no-referrer"></p> 
    <p>参数化且应用了加密算法后打 印出来的值</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-6bb8667e7bb6fcb86983c684b50a97f6e45.png" referrerpolicy="no-referrer"></p> 
    <p>按接口参数依赖关系 推导出来的接口依赖，建测试场景时，自动加入所依赖的接口，并按依赖关系排好执行顺序</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-4c98db927c793fd0f3f830a3ee2d22a63d5.png" referrerpolicy="no-referrer"></p> 
    <p>这是mock 的一个接口，josn 数据是加密了的，</p> 
    <p>第一次测试这接口我没加解密算法</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-54e3b67d553bc466fdeb8dd19c87aaab67b.png" referrerpolicy="no-referrer"></p> 
    <p>第一次测试这接口解密算法</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-32f9bb52d64bef78b74facba654bae707b8.png" referrerpolicy="no-referrer"></p> 
    <p>响应是密文</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-7d9582adbf31e316d6c95e2ca1d78363af5.png" referrerpolicy="no-referrer"></p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-5c29d4da0fc9d57f708082917057b7e6994.png" referrerpolicy="no-referrer"></p> 
    <p>维护好解密算法</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-85a089245ff393a40645c0dc1c2aa1565c3.png" referrerpolicy="no-referrer"></p> 
    <p>之前的接口中选这个解密</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-4ec0a2aa95e0a14805ac18f7cfd0243c1c6.png" referrerpolicy="no-referrer"></p> 
    <p>再测试，接口的结果解密了</p> 
    <p><img src="https://oscimg.oschina.net/oscnet/up-b33f6e8b9d00f6467acc17220f2311a731c.png" referrerpolicy="no-referrer"></p> 
    <p>mock 支持上图4种延时</p> 
    <p><strong>五：功能概<strong>览</strong></strong></p> 
   </div> 
   <p><strong>（一）接口测试 功能概<strong>览</strong>：</strong></p> 
   <p><strong>         基本流程：</strong> (1)BaseUrl 设置------>(2)基础认证设置 ----->（3）接口安全设置------>（4）维护接口用例----->（5）拖拽生成接口断言------>    (6)建接口测试场景(可在迭代中直接增加)--->(7)手动执行接口测试场景(可单个，也可一键执行场景中所有接口)或定时执行测试场景。另外还有接口mock</p> 
   <p><strong>       1:接口测试总览</strong></p> 
   <p><strong><img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812114654659-1192785390.png" referrerpolicy="no-referrer"></strong></p> 
   <p>      <strong>  2:全局设置</strong></p> 
   <p><img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812113618517-471109410.png" referrerpolicy="no-referrer"></p> 
   <p> <strong>3:接口按全设置</strong></p> 
   <p>维护好接口的加密，解密及签名 ，上传相关类或JAR ，在接口用例中选维护好的加密，解密及签名,供itest 执行接口测试时来回调<strong> ,</strong></p> 
   <p><strong><img alt src="https://img2020.cnblogs.com/blog/261867/202011/261867-20201119123909003-1707110134.png" referrerpolicy="no-referrer"></strong></p> 
   <p> </p> 
   <p> <img alt src="https://img2020.cnblogs.com/blog/261867/202011/261867-20201119124238708-1445715765.png" referrerpolicy="no-referrer"></p> 
   <p> 4<strong>:接口用例维护</strong></p> 
   <p>   接口参数维护，非常方便  ，对测试人员友好,</p> 
   <p><img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812112411537-1450698142.png" referrerpolicy="no-referrer"></p> 
   <p>上图用的6.6.6版本的，7.0.0后还可选加密解密签名算法</p> 
   <p><strong><img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812111746583-2057801361.png" referrerpolicy="no-referrer"></strong></p> 
   <p>上图用的6.6.6版本的，7.0.0后还可选加密解密签名算法</p> 
   <p> </p> 
   <p> <img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812111952601-1020885275.png" referrerpolicy="no-referrer"></p> 
   <p>上图用的6.6.6版本的，7.0.0后还可选加密解密签名算法</p> 
   <p><strong>5:拖拽式断言设置</strong></p> 
   <p><img src="https://oscimg.oschina.net/oscnet/up-3840f37dbcf5381d3d7fa07ac12d66f8ad4.png" referrerpolicy="no-referrer"></p> 
   <p><img src="https://oscimg.oschina.net/oscnet/up-3297dc87432d97cf1b77a1e0f26e07d92db.png" referrerpolicy="no-referrer"></p> 
   <p><img src="https://oscimg.oschina.net/oscnet/up-0d46b38fd5757e6f21a9b3e2f12af447547.png" referrerpolicy="no-referrer"></p> 
   <p><img src="https://oscimg.oschina.net/oscnet/up-5faa88162b5a124e4391172bcacc7340988.png" referrerpolicy="no-referrer"></p> 
   <p><strong>6：接口场景</strong></p> 
   <p><img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812114129798-2130450352.png" referrerpolicy="no-referrer"></p> 
   <p> 在场景中可单个，也可一键执行所有接口用例，也可手动调整执行顺序</p> 
   <p><img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812114442070-745612531.png" referrerpolicy="no-referrer"></p> 
   <p><strong>7:接口执行日志</strong></p> 
   <p><img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812115124424-579721645.png" referrerpolicy="no-referrer"></p> 
   <p><strong>8:定时执行接口测试场景</strong></p> 
   <p><strong>      <img alt src="https://img2020.cnblogs.com/blog/261867/202008/261867-20200812122157831-1835512598.png" referrerpolicy="no-referrer"></strong></p> 
   <p><strong>9:接口mock</strong></p> 
   <p><img alt src="https://img2020.cnblogs.com/blog/261867/202011/261867-20201119123644465-708159450.png" referrerpolicy="no-referrer"></p> 
   <div> 
    <p><strong>(二)产品截图及其他功能概览</strong></p> 
    <div> 
     <p><img alt src="https://img2018.cnblogs.com/blog/261867/201910/261867-20191030191821540-1523941801.png" referrerpolicy="no-referrer"></p> 
     <p> 可线下离线处理测试用例，再同步到线上，</p> 
     <p><img alt src="https://img2018.cnblogs.com/blog/261867/201910/261867-20191030191832096-975330038.png" referrerpolicy="no-referrer"></p> 
     <p><img alt src="https://img2018.cnblogs.com/blog/261867/201910/261867-20191030191839563-1712160986.png" referrerpolicy="no-referrer"></p> 
     <p><img alt src="https://oscimg.oschina.net/oscnet/up-c85bd31b7c14d2097023eeca3973049f82c.png" referrerpolicy="no-referrer"></p> 
     <p>除了可同步线下执行，还支持多种导入，在用例BUG统计示图中，测试需求分解对上，</p> 
     <p>每个模块上显示BUG数和用例数</p> 
     <p><img alt src="https://oscimg.oschina.net/oscnet/up-ad2342b13f0b2f65a7255fd96ec7a334870.png" referrerpolicy="no-referrer"></p> 
     <p>用例库维护公共用例，在项目中可以从用例库或是EXCEL呀是xmind 中导入用例,且在导入时，如需求项，用例分类，优先级，以及用例标签 ，如系统中不存在，会自动在导入时建立</p> 
     <p>可按测试包分配测试任务，通过把多个测试包加到测试迭代中，统计测试执行情况</p> 
     <p><img alt height="303" src="https://img2020.cnblogs.com/blog/261867/202009/261867-20200920225715820-1286544068.png" width="700" referrerpolicy="no-referrer"></p> 
     <p><img alt height="394" src="https://oscimg.oschina.net/oscnet/c358b0870c69c28759b2290cba35a3071b0.jpg" width="700" referrerpolicy="no-referrer"></p> 
     <div>
      <img height="593" src="https://oscimg.oschina.net/oscnet/up-a624369d7b22448cd41b366171e6991d56b.png" width="700" referrerpolicy="no-referrer">
     </div> 
     <div>
      在迭代中 直接建测试包， 方便一气呵成分配测试任务,且可快捷分配测试用例到用例包中，还可在迭代测试包TAB中，二次分配测试包中，测试用例　　
     </div> 
     <p><img alt height="362" src="https://oscimg.oschina.net/oscnet/up-7b5210da0b7ab48561ee2df81d28d626ad6.png" width="700" referrerpolicy="no-referrer"></p> 
     <p>执行测试用例包任务</p> 
     <p>可在看板上，填写任务进度，执行测试用例包，或是处理流转到名下的BUG</p> 
     <p><img alt height="314" src="https://oscimg.oschina.net/oscnet/up-df56d589b8f1e3cb5ea7e4a9c0a341a8d15.png" width="700" referrerpolicy="no-referrer"></p> 
     <p><img alt height="319" src="https://oscimg.oschina.net/oscnet/15cc6cb36931b4274bf9d930576df50993c.jpg" width="700" referrerpolicy="no-referrer"></p> 
     <p>在看板上，直接可以执行用例</p> 
     <p><img alt height="388" src="https://img2020.cnblogs.com/blog/261867/202009/261867-20200920230619395-1296087220.png" width="700" referrerpolicy="no-referrer"></p> 
     <p> 用例执行页面，增加一个转BUG的功能，方便执行时直接转BUG，且自动测试用例为不通过，之前是在用例包用例列表页面点用例ID，<br> 不便于看用例的具体内容，这是6.6.2 第2个迫切便捷功能</p> 
     <p> </p> 
     <p><strong>流程驱动测试</strong></p> 
     <p>流程驱动缺陷在26种状态中演化，更精准反正工作实况</p> 
     <p>测试流程引擎自动推算可演化状态及流转到谁名下，且可实时调整流程</p> 
     <p> <img alt height="405" src="https://img2018.cnblogs.com/blog/261867/201911/261867-20191128101319990-309591461.png" width="700" referrerpolicy="no-referrer"></p> 
     <p><strong>从 BUG的邮件通知中连BUG链接，可能直接处理BUG</strong></p> 
     <p><img alt height="305" src="https://oscimg.oschina.net/oscnet/up-28c0dcd8c23b6c5dc831aef888be79c610d.png" width="700" referrerpolicy="no-referrer"></p> 
     <p style="text-align:justify">在收到的BUG邮件中，带一个连接，一点就自动登录ITEST，同时，弹出邮件中的BUG处理界面</p> 
     <p><strong><strong>多维度测试度量</strong></strong></p> 
     <p>趋势分析洞察研发过程潜在风险，为项目管控提供决策依据</p> 
     <p>结果数据分析掌控团队效率，为持续改进提供量化数据支持</p> 
     <p>测试总揽，测试经理每日工作复盘好帮手，量化的测试日报</p> 
     <p> <img alt height="401" src="https://img2018.cnblogs.com/i-beta/261867/202002/261867-20200213105655644-1416286452.png" width="700" referrerpolicy="no-referrer"></p> 
     <p> <img alt height="317" src="https://oscimg.oschina.net/oscnet/b553f72f092cda8fe36953d14654e91d8b8.jpg" width="700" referrerpolicy="no-referrer"></p> 
     <p>测试人员简报： 里面有测试人员写用例情况，执行用例情况，提交的 BUG数，提交的BUG 按</p> 
     <p>状态按人分布，提交的BUG按类型按人分布，提交的BUG按等级按人分布，且可按不同版本作</p> 
     <p>为条件进行分析 </p> 
     <p><img alt height="421" src="https://oscimg.oschina.net/oscnet/up-f0627e10ecb672f24e3aa8a3fd1180db8a6.png" width="700" referrerpolicy="no-referrer"></p> 
     <p><img alt height="408" src="https://oscimg.oschina.net/oscnet/up-6549941126d062f130fa866f241888b57cc.png" width="700" referrerpolicy="no-referrer"></p> 
     <p>开发人员处理BUG简报 ： 有开发人员BUG数统计， 也有按bug状态按人分布，按bug等级按人分布，</p> 
     <p>按bug类型按人分布,按人按BUG 龄期分布(龄期可按天也可按周计)，且可按不同版本作为条件进行分析</p> 
     <p><img alt height="419" src="https://oscimg.oschina.net/oscnet/up-9b6c7fd7c7c742ac96911b6e7aa050188b0.png" width="700" referrerpolicy="no-referrer"></p> 
     <p><img alt height="399" src="https://oscimg.oschina.net/oscnet/up-357be0c4bf4ed5d5fb05e1c6dadcd09a988.png" width="700" referrerpolicy="no-referrer"></p> 
     <p><strong><strong><strong>测试环境维护</strong></strong></strong></p> 
     <p><strong><strong><strong><img alt height="326" src="https://img2018.cnblogs.com/blog/261867/201911/261867-20191128101009263-1761168980.png" width="700" referrerpolicy="no-referrer"></strong></strong></strong></p> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            