
---
title: 'PowerShell v7.1.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5321'
author: 开源中国
comments: false
date: Tue, 17 Aug 2021 06:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5321'
---

<div>   
<div class="content">
                                                                                            <p>PowerShell v7.1.4 现已发布。PowerShell Core 是跨平台的（Windows，Linux和macOS）自动化和配置工具/框架，可与现有的工具配合使用，并针对处理结构化数据（例如 JSON，CSV，XML 等）、REST API 和对象模型进行了优化。它包括命令行 Shell、关联的脚本语言和用于处理 cmdlet 的框架。 </p> 
<p>具体更新内容如下：</p> 
<p><strong>构建和打包改进</strong></p> 
<ul> 
 <li>将 .NET SDK 升级到 5.0.400 版本 
  <ul> 
   <li>从<code>PSDesiredStateConfiguration</code>模块中删除 cat 文件（Internal 16723）</li> 
   <li>更新 .NET SDK 版本和其他包（Internal 16715）</li> 
  </ul> </li> 
</ul> 
<p><strong>SHA256 Hashes of the release artifacts</strong></p> 
<ul> 
 <li>powershell_7.1.4-1.debian.10_amd64.deb 
  <ul> 
   <li>BC3D741F026BE966DE641EA305E73701AAE61DA16AA1618A4500EAE8B92FB69D</li> 
  </ul> </li> 
 <li>powershell_7.1.4-1.debian.11_amd64.deb 
  <ul> 
   <li>E3DEA08EDCE931DE695AFBF021134C02407293770788272F301E8E39C4C3FFE2</li> 
  </ul> </li> 
 <li>powershell_7.1.4-1.debian.9_amd64.deb 
  <ul> 
   <li>14D042403F19B63A6508EC51521B00F0F3CF80B3B20753C547725ADCD8C95E84</li> 
  </ul> </li> 
 <li>powershell_7.1.4-1.ubuntu.16.04_amd64.deb 
  <ul> 
   <li>BDB45D6CA0CC99D6A9E5876E9B325586A74823474E62E987B4C30C19612D7923</li> 
  </ul> </li> 
 <li>powershell_7.1.4-1.ubuntu.18.04_amd64.deb 
  <ul> 
   <li>D6663A841E7318023D7852B7539580610170A713778257DF325934DFAE39CE4B</li> 
  </ul> </li> 
 <li>powershell_7.1.4-1.ubuntu.20.04_amd64.deb 
  <ul> 
   <li>7435B5CDD8CBEDEEE396072B495B44067166674E7C40A9EE844A519C6223E482</li> 
  </ul> </li> 
 <li>powershell-7.1.4-1.centos.8.x86_64.rpm 
  <ul> 
   <li>5BCA9B5FDDB2AA6AE477D070A71D331876E6465CEA5CAA228505B84ACB166D7C</li> 
  </ul> </li> 
 <li>powershell-7.1.4-1.rhel.7.x86_64.rpm 
  <ul> 
   <li>3F4E0A52DECCD179E6817F5123AD1E94BAB841B55288A4524AAAD8A230BD5A84</li> 
  </ul> </li> 
 <li>powershell-7.1.4-linux-alpine-x64.tar.gz 
  <ul> 
   <li>289BF62DA59E5E763CE8BC763A36FC584B524BDA1ECE6FD5BF1C09CF00D0AC2E</li> 
  </ul> </li> 
 <li>powershell-7.1.4-linux-arm32.tar.gz 
  <ul> 
   <li>2B2B55BF690B58A8DBBD1ABDE6B2C001C351FF33D4473C6D80AE9A6B6F469D54</li> 
  </ul> </li> 
 <li>powershell-7.1.4-linux-arm64.tar.gz 
  <ul> 
   <li>65B65BEEF80E0325C1025C6189320FC9F4345C31B2E3A9A13FC2C70283776D4E</li> 
  </ul> </li> 
 <li>powershell-7.1.4-linux-x64.tar.gz 
  <ul> 
   <li>250A9C3767896A94F74BBE41CC8FD60048D9B7EFD4EEA4D2325B45716D1C4BAA</li> 
  </ul> </li> 
 <li>powershell-7.1.4-linux-x64-fxdependent.tar.gz 
  <ul> 
   <li>C60D9386191956FA52B8C3A5E4E7F4B5AF15930E794441BA6A3E872CA52A43EF</li> 
  </ul> </li> 
 <li>powershell-7.1.4-osx-x64.pkg 
  <ul> 
   <li>66AC3BC82C83B8F2864BF5EA20C67538C7B51AE25E6A9178F930BCDC35A12D9A</li> 
  </ul> </li> 
 <li>powershell-7.1.4-osx-x64.tar.gz 
  <ul> 
   <li>182D3E2DDFD581725D82199D3628FD5E18CDCD4346DE2FCA99AE4927835451EB</li> 
  </ul> </li> 
 <li>PowerShell-7.1.4-win-arm32.zip 
  <ul> 
   <li>5EC02D49ED7261AACE410D911A040982C46DB04DEA3017536AC198DD61969672</li> 
  </ul> </li> 
 <li>PowerShell-7.1.4-win-arm64.zip 
  <ul> 
   <li>345F4B16E5DAA0C2C6D2CB0758098B39B2FDB26D5C8B181FF16424B6C37C529F</li> 
  </ul> </li> 
 <li>PowerShell-7.1.4-win-fxdependent.zip 
  <ul> 
   <li>C4A118A87193893465849D859B4BE042CC959D00EC87D206E19CB71143E2FADF</li> 
  </ul> </li> 
 <li>PowerShell-7.1.4-win-fxdependentWinDesktop.zip 
  <ul> 
   <li>766D7A175F87D97D084371FEA7A9A24D303C4D9BCB1BCD33C58E3C8E824480DE</li> 
  </ul> </li> 
 <li>PowerShell-7.1.4-win-x64.msi 
  <ul> 
   <li>9190F005ADCC59F1D2CFF21B8D4FBBA70D72B8B4B567D845B33508A9C388A7A2</li> 
  </ul> </li> 
 <li>PowerShell-7.1.4-win-x64.zip 
  <ul> 
   <li>EC5792D74EAE88601D20734C857212920135AA5899823DCAF1C0143DAEDD8108</li> 
  </ul> </li> 
 <li>PowerShell-7.1.4-win-x86.msi 
  <ul> 
   <li>E75859850B7E7E6A3ACB7A33F1F33171A77636CB8944CEA11FB2E9C0537416B5</li> 
  </ul> </li> 
 <li>PowerShell-7.1.4-win-x86.zip 
  <ul> 
   <li>B44702F129514E638798D62A6F3EACB62EF8A628052F71F1CEED179EDE3D4564</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPowerShell%2FPowerShell%2Freleases%2Ftag%2Fv7.1.4" target="_blank">https://github.com/PowerShell/PowerShell/releases/tag/v7.1.4</a></p>
                                        </div>
                                      
</div>
            