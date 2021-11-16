
---
title: 'openGauss 支持国密 SM3 和 SM4 算法'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1116/141234_JZw9_5430600.jpg'
author: 开源中国
comments: false
date: Tue, 16 Nov 2021 06:21:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1116/141234_JZw9_5430600.jpg'
---

<div>   
<div class="content">
                                                                                            <h2><strong>1. 国密算法介绍</strong></h2> 
<p><span>国</span><span>密即国家密码局认定的国产密码算法，常用的算法有 SM1，SM2，SM3，SM4，其中密钥长度和分组长度均为 128 位。</span><span>针对银行客户对数据库安全能力的诉求以及提高产品安全竞争力的要求，进行数据库企业级安全能力增强，openGauss 自 2.0.0版本 支持了国密</span><span>算法，主要包括用户认证支持国密SM3算法</span><span>，支持利用国密 SM4 算法对数据进行加解密。</span></p> 
<h2><strong style="color:#333333">2. 国密 SM3 算法——用户认证</strong></h2> 
<h3><strong style="color:#2d2d2d">2.1 使用方法</strong></h3> 
<p style="margin-left:0; margin-right:0">openGauss现支持四种用户认证方式，其通过postgresql.conf文件中的参数password_encryption_type确定，认证方式与该参数的对应关系如下表所示：</p> 
<table cellspacing="0" style="border-collapse:collapse; box-sizing:border-box !important; display:table; margin:0px 0px 10px; max-width:100%; outline:0px; overflow-wrap:break-word !important; padding:0px; width:676.571px"> 
 <tbody> 
  <tr> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0">认证方式</p> </td> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:left">参数</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0">md5</p> </td> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:left">password_encryption_type=0</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0">sha256+md5</p> </td> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:left">password_encryption_type=1</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0">sha256</p> </td> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:left">password_encryption_type=2</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0">sm3</p> </td> 
   <td colspan="1" rowspan="1" style="background-color:#ffffff; border-color:#3e3e3e; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:left">password_encryption_type=3</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="margin-left:0; margin-right:0">其中 SM3 认证算法目前只支持 gsql、 JDBC、 ODBC 三种连接方式。</p> 
<p style="margin-left:0; margin-right:0">创建SM3认证方式的用户的步骤：</p> 
<p style="margin-left:0; margin-right:0">（1）在 postgresql.conf 文件中配置 password_encryption_type=3，并重启数据库使该参数生效，则之后创建的用户将采用 SM3 算法进行明文密码的加密。</p> 
<p><img alt height="13" src="https://static.oschina.net/uploads/space/2021/1116/141234_JZw9_5430600.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">（2）创建用户</p> 
<p style="margin-left:0; margin-right:0">如下示例中，创建了test用户，通过系统表pg_authid的rolpassword字段可以查看用户创建时对应的加密方式，图示即对应SM3加密</p> 
<p><img alt height="69" src="https://static.oschina.net/uploads/space/2021/1116/141355_Ujt5_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">（3）在 pg_hba.conf 文件中配置认证方式为 SM3</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="112" src="https://static.oschina.net/uploads/space/2021/1116/141448_w52o_5430600.jpg" width="700" referrerpolicy="no-referrer"></span></p> 
<p><span style="background-color:#ffffff; color:#333333">此时test用户远程登录方可认证通过</span></p> 
<p><img alt height="79" src="https://static.oschina.net/uploads/space/2021/1116/141501_3cfl_5430600.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对于利用SM3加密算法创建的用户，只有加密算法和认证方式均为SM3算法时，认证才会通过。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">针对SM3用户，当通过JDBC远程连接时，需手动下载Jar包bcprov-jdk15on，并导入至应用程序中。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载：<span>https://mvnrepository.com/artifact/org.bouncycastle/bcprov-jdk15on/1.68</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对于创建其他认证方式的用户，过程与SM3类似，此处不再赘述。</p> 
<h3><strong style="color:#2d2d2d">2.2 实现原理</strong></h3> 
<p><span style="background-color:#ffffff; color:#333333">openGauss 使用 RFC5802 口令认证方案</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>用户秘钥生成</strong></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">RFC5802秘钥衍生过程如下图所示<br> <img alt height="449" src="https://static.oschina.net/uploads/space/2021/1116/141610_seiG_5430600.jpg" width="500" referrerpolicy="no-referrer"></p> 
<pre style="margin-left:0; margin-right:0; text-align:justify"><code><span>SaltedPassword := PBKDF2 (password, salt, i)</span></code><code><span>  ClientKey := HMAC(SaltedPassword, "Client Key")</span></code><code><span>  StoredKey := Hash(ClientKey)</span></code></pre> 
<p style="margin-left:0; margin-right:0">服务器端存的是StoredKey和ServerKey:</p> 
<p style="margin-left:0; margin-right:0">1）StoredKey是用来验证Client客户身份的</p> 
<p style="margin-left:0; margin-right:0">服务端认证客户端通过计算ClientSignature与客户端发来的ClientProof进行异或运算，从而恢复得到ClientKey，然后将其进行hash运算，将得到的值与StoredKey进行对比。如果相等，证明客户端验证通过。</p> 
<p style="margin-left:0; margin-right:0; text-align:left">2）ServerKey是用来向客户端表明自己身份的</p> 
<p style="margin-left:0; margin-right:0">类似的，客户端认证服务端，通过计算ServerSignature与服务端发来的值进行比较，如果相等，则完成对服务端的认证。</p> 
<p style="margin-left:0; margin-right:0">3）在认证过程中，服务端可以计算出来ClientKey，验证完后直接丢弃不必存储。</p> 
<p style="margin-left:0; margin-right:0">要做到合法的登录，必须知道Password、SaltedPassword或者ClientKey。如果StoryKey和ServerKey泄露，无法做到合法登录。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>认证流程</strong></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">标准RFC5802口令认证流程如下图所示：</p> 
<p><br> <img alt height="411" src="https://static.oschina.net/uploads/space/2021/1116/141644_Wk8F_5430600.jpg" width="500" referrerpolicy="no-referrer"></p> 
<p><strong>说明：</strong></p> 
<ol> 
 <li style="text-align:left">客户端发送username给服务端。</li> 
 <li style="text-align:left">服务端返回给客户端AuthMessage 和计算出来的ServerSignature。</li> 
 <li style="text-align:left">客户端收到信息后，首先利用认证信息AuthMessage中的salt和iteration-count(迭代次数)，从password计算得到SaltedPassword，然后计算得到下层所有的key。计算HMAC(ServerKey, AuthMessage) == ServerSignature是否相等，如果相等，则client完成对服务端的认证。</li> 
 <li style="text-align:left">客户端将计算得到的ClientProof发送给服务端。</li> 
 <li style="text-align:left">服务端使用其保存的StoredKey和AuthMessage计算HMAC，在和接收的client发送的ClientProof进行异或，得到ClientKey，在对ClientKey进行哈希，和其保存的StoredKey进行比较是否一致。如果一致，则客户端的认证通过。</li> 
</ol> 
<p style="color:rgba(62, 62, 62, 0.7); margin-left:0px; margin-right:0px; text-align:left">服务器端收到客户端请求后，根据 pg_hba.conf  配置的认证方式，与客户端进行相应的认证交互。</p> 
<p style="margin-left:0; margin-right:0"><strong>3. 国密SM4算法——数据加解密</strong></p> 
<p>SM4国密算法可用于对表中的某一列数据进行加解密。参考gs_encrypt_aes128加密函数、gs_decrypt_aes128解密函数，新增的加密函数gs_encrypt，解密函数gs_decrypt支持aes128、sm4的加解密，可以兼容aes128。其中SM4算法调用openssl中的EVP_sm4_cbc()接口。</p> 
<p style="margin-left:0; margin-right:0"><strong>gs_encrypt_aes128和gs_decrypt_aes128函数示意：</strong></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#dddddd">- gs_encrypt_aes128(encryptstr, keystr)</span></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#dddddd">       描述：以keystr为密钥对encryptstr字符串进行加密，返回加密后的字符串。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#dddddd">- gs_decrypt_aes128(decryptstr,keystr)       </span></p> 
<p style="margin-left:0; margin-right:0"><span style="background-color:#dddddd">       描述：以keystr为密钥对decryptstr字符串进行解密，返回解密后的字符串</span></p> 
<p><img alt height="108" src="https://static.oschina.net/uploads/space/2021/1116/141839_i1aQ_5430600.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>gs_encrypt和gs_decrypt函数示意：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#dddddd">- gs_encrypt(encryptstr, keystr, algorithm)</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#dddddd">      描述：以keystr为密钥对encryptstr字符串利用algorithm进行加密，返回加密后的字符串。可选的algorithm为sm4和aes128。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#dddddd">- gs_decrypt(decryptstr,keystr, algorithm)</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#dddddd">       描述：以keystr为密钥对decryptstr字符串利用algorithm进行解密，返回解密后的字符串。可选的algorithm为sm4和aes128。</span></p> 
<p><img alt height="226" src="https://static.oschina.net/uploads/space/2021/1116/141912_xSbB_5430600.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p><strong style="color:#333333"><span>利用SM4算法对表中数据进行加解密示意图：</span></strong></p> 
<p><img alt height="221" src="https://static.oschina.net/uploads/space/2021/1116/141938_X09I_5430600.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p><img alt height="352" src="https://static.oschina.net/uploads/space/2021/1116/142003_ukjH_5430600.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">至此，openGauss 支持使用国密 SM3 算法进行用户认证，SM4 算法进行数据加解密。</span></p>
                                        </div>
                                      
</div>
            