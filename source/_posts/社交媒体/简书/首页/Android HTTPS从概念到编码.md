
---
title: 'Android HTTPS从概念到编码'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/3415839-487d566745447653.jpg'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/3415839-487d566745447653.jpg'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="533" data-height="300"><img data-original-src="//upload-images.jianshu.io/upload_images/3415839-487d566745447653.jpg" data-original-width="533" data-original-height="300" data-original-format="image/jpeg" data-original-filesize="10456" src="https://upload-images.jianshu.io/upload_images/3415839-487d566745447653.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>HTTPS请求为什么就安全？</h3>
<p>https是一个建立在密码学基础之上的一种安全通信协议，准确来说是基于HTTP协议和SSL/TSL的组合，要想理解HTTPS必须了解密码学的一些相关基础概念。</p>
<h4>公钥密码体制</h4>
<p>公钥密码体制分为三个部分，公钥，私钥，加密解密算法，加密解密过程如下：</p>
<ul>
<li>加密：通过加密算法和公钥对内容(或者说明文)进行加密，得到密文。加密过程需要用到公钥。</li>
<li>解密：通过解密算法和私钥对密文进行解密，得到明文。解密过程需要用到解密算法和私钥。<strong>注意，由公钥加密的内容，只能由私钥进行解密，也就是说，由公钥加密的内容，如果不知道私钥，是无法解密的</strong>。</li>
</ul>
<h4>对称加密算法</h4>
<p>在对称加密算法中，加密使用的密钥和解密使用的密钥是相同的。也就是说，加密和解密都是使用的同一个密钥。因此对称加密算法要保证安全性的话，密钥要做好保密，只能让使用的人知道，不能对外公开。这个和上面的公钥密码体制有所不同，公钥密码体制中加密是用公钥，解密使用私钥，而对称加密算法中，加密和解密都是使用同一个密钥，不区分公钥和私钥。 密钥，一般就是一个字符串或数字，在加密或者解密时传递给加密/解密算法。前面在公钥密码体制中说到的公钥、私钥就是密钥，公钥是加密使用的密钥，私钥是解密使用的密钥。</p>
<h4>RSA简介</h4>
<p>RSA密码体制是一种公钥密码体制，公钥公开，私钥保密，它的<strong>加密解密算法是公开的</strong>。 由公钥加密的内容可以并且只能由私钥进行解密，并且由私钥加密的内容可以并且只能由公钥进行解密。也就是说，RSA的这一对公钥、私钥<strong>都可以</strong>用来加密和解密，并且一方加密的内容可以由并且只能由对方进行解密。</p>
<h4>非对称加密算法</h4>
<p>在非对称加密算法中，加密使用的密钥和解密<strong>使用的密钥是不相同的</strong>。前面所说的公钥密码体制就是一种非对称加密算法，他的公钥和是私钥是不能相同的，也就是说加密使用的密钥和解密使用的密钥不同，因此它是一个非对称加密算法。</p>
<p>了解了以上的基础概念之后我们就可以聊聊为什么安全了，这里我们就可以笼统的讲一下当我们打开一个https链接的时候发生了什么事情。</p>
<ol>
<li>当我们在通信过程开始时，会收到服务器的证书。</li>
<li>首先应用程序读取证书中的Issuer(发布机构)，然后会在应用程序的系统中受信任的发布机构的证书中去找。</li>
<li>如果找不到，那证书可能有问题，程序会给出一个错误信息。</li>
<li>如果在系统中找到这个证书的发布机构，那么应用程序就会从证书中取出这个机构证书的公钥。</li>
<li>然后对服务器下发的证书里面的指纹和指纹算法用这个公钥进行解密，然后使用指纹算法计算服务器下发证书中的指纹。将这个计算的指纹与放在证书中的指纹对比。（<strong>非对称加密</strong>）</li>
<li>如果一致说明服务器下发的证书是通过通过机构发布的。然后就可以保证通信安全了。</li>
<li>然后这时候应用程序选择一个对称加密算法和一个秘钥，用公钥加密之后发送给服务器。</li>
<li>服务器收到后使用私钥解密，获取秘钥，本次通话会从现在开始，通过<strong>对称加密</strong>算法进行通信。</li>
</ol>
<p>通过上诉简单的描述，也可了解到https通信是是通过各种加密算法及证书比对校验完成的一个http通信。</p>
<h3>SSL/TLS证书？</h3>
<p>ssl Secure Sockets Layer,现在应该叫"TLS",但由于习惯问题,我们还是叫"SSL"比较多，ssl证书是数字证书的一种，数字证书有较多的内容项，里面的内容比较多——Version、Serial number、Signature algorithm 等等，挑几个重要的解释一下。</p>
<ul>
<li>Issuer (证书的发布机构)<br>
指出是什么机构发布的这个证书，也就是指明这个证书是哪个公司创建的(只是创建证书，不是指证书的使用者)</li>
<li>Valid from , Valid to (证书的有效期)<br>
也就是证书的有效时间，或者说证书的使用期限。 过了有效期限，证书就会作废，不能使用了。</li>
<li>Public key (公钥)<br>
这个我们在前面介绍公钥密码体制时介绍过，公钥是用来对消息进行加密的</li>
<li>Subject (主题)<br>
这个证书是发布给谁的，或者说证书的所有者，一般是某个人或者某个公司名称、机构的名称、公司网站的网址等。 对于这里的证书来说，证书的所有者是Trustwave这个公司。</li>
<li>Signature algorithm (签名所使用的算法)<br>
就是指的这个数字证书的数字签名所使用的加密算法，这样就可以使用证书发布机构的证书里面的公钥，根据这个算法对指纹进行解密。指纹的加密结果就是数字签名。</li>
<li>Thumbprint, Thumbprint algorithm (指纹以及指纹算法)<br>
这个是用来保证证书的完整性的，也就是说确保证书没有被修改过。 其原理就是在发布证书时，发布者根据指纹算法(一个hash算法)计算整个证书的hash值(指纹)并和证书放在一起，使用者在打开证书时，自己也根据指纹算法计算一下证书的hash值(指纹)，如果和刚开始的值对得上，就说明证书没有被修改过，因为证书的内容被修改后，根据证书的内容计算的出的hash值(指纹)是会变化的。 注意，这个指纹会使用"SecureTrust CA"这个证书机构的私钥用签名算法(Signature algorithm)加密后和证书放在一起。</li>
</ul>
<h4>证书颁发机构（CA）</h4>
<p>·Symantec (which bought VeriSign's SSL interests and owns Thawte and Geotrust) 38.1% 市场份额</p>
<p>·Comodo SSL 29.1%</p>
<p>·Go Daddy 13.4%</p>
<p>·GlobalSign 10%</p>
<p>安卓系统中, 你可以在下列路径中找到证书颁发机构:   设置 -> 安全 -> 受信任的凭证</p>
<p>最佳和最安全的私钥获取方法是向可信任的证书颁发机构 (CA)（例如将带您完成身份验证过程的赛门铁克公司）申请一个证书。一旦有了自己的证书，就可以生成您自己的私钥。您可以使用该私钥为您的可执行文件或软件库签名，私钥仅可通过可追溯到 CA 的公钥解锁，而公钥已预安装在大部分浏览器中。如果在签名后代码被篡改，公钥将不能核实私钥签名的真实性，浏览器将立即向任何尝试下载代码的人弹出警告窗口。如果代码完好无损，则将提供您的文。</p>
<h4>什么是自签名证书？</h4>
<p>自签名证书就是没有通过受信任的证书颁发机构, 自己给自己颁发的证书.</p>
<p>SSL 证书大致分三类:</p>
<ul>
<li>由安卓认可的证书颁发机构(如: VeriSign), 或这些机构的下属机构颁发的证书.</li>
<li>没有得到安卓认可的证书颁发机构颁发的证书.</li>
<li>自己颁发的证书, 分临时性的(在开发阶段使用)或在发布的产品中永久性使用的两种.</li>
</ul>
<h4>X.509 又是什么</h4>
<p>X.509 - 这是一种证书标准,主要定义了证书中应该包含哪些内容.其详情可以参考RFC5280,<strong>SSL/TLS使用的就是这种证书标准</strong>.</p>
<h5>编码格式</h5>
<p>同样的X.509证书,可能有不同的编码格式,目前有以下两种编码格式.</p>
<p>PEM - Privacy Enhanced Mail,打开看文本格式,以"-----BEGIN..."开头, "-----END..."结尾,内容是BASE64编码.<br>
查看PEM格式证书的信息:openssl x509 -in certificate.pem -text -noout<br>
Apache和*NIX服务器偏向于使用这种编码格式.</p>
<p>DER - Distinguished Encoding Rules,打开看是二进制格式,不可读.<br>
查看DER格式证书的信息:openssl x509 -in certificate.der -inform der -text -noout<br>
Java和Windows服务器偏向于使用这种编码格式.</p>
<h6>KeyStore</h6>
<p>在 Android 和 java中 更多的是使用keystore。最常用的工具就是keytool.<br>
Keytool是一个Java数据证书的管理工具 ,Keytool将密钥（key）和证书（certificates）存在一个称为keystore的文件中。<br>
在keystore里，包含两种数据：</p>
<ol>
<li>密钥实体（KeyEntry）——密钥（secret key）</li>
<li>可信任的证书实体（CertEntry）——只包含公钥</li>
</ol>
<p>每个keystore都关联这一个独一无二的alias，这个alias通常不区分大小写</p>
<h3>Android 中如何配置SSL/TLS</h3>
<p>以上所述皆是对HTTPS SSL/TLS的概念叙述，通过这个描述会让你对下面的配置以及编码更加了解。我们在Android 开发中配置项目支持HTTPS这是个基本的操作。下面我会以OkHttp网络框架为例。通过以下三点可完成项目配置。</p>
<ol>
<li>如何配置系统、用户信任证书校验？</li>
<li>自签名证书如何在项目中配置？</li>
<li>如何通过配置文件进行配置SSL/TLS证书？</li>
</ol>
<h4>如何配置系统、用户信任证书校验？</h4>
<p>Android OkHttp框架默认是提供了对系统用户信任证书的校验。如果服务器下发的证书是被Android信任机构颁发的证书是不会出现安全提示的，或者是用户添加到系统的证书也是不会出现任何安全提示。</p>
<p>在 AOSP 源码库中，CA 根证书主要存放在 system/ca-certificates 目录下，而在 Android 系统中，则存放在 /system/etc/security/ 目录下。所以我们没有Root的手机是无法进行添加根证书的。</p>
<p>也可以根据以下配置进行系统根证书安全校验</p>
<pre><code>public static SSLSocketFactory getSSLSocketFactory() &#123;
        SSLSocketFactory ssfFactory = null;
        SSLContext sc = null;
        try &#123;
            sc = SSLContext.getInstance("TLS");
            TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(
                    TrustManagerFactory.getDefaultAlgorithm());
            trustManagerFactory.init((KeyStore) null);

            sc.init((KeyManager[]) null,  trustManagerFactory.getTrustManagers(), new SecureRandom());
            ssfFactory = sc.getSocketFactory();
        &#125; catch (NoSuchAlgorithmException e) &#123;
            e.printStackTrace();
        &#125; catch (KeyManagementException e) &#123;
            e.printStackTrace();
        &#125; catch (KeyStoreException e) &#123;
            e.printStackTrace();
        &#125;
        return ssfFactory;
    &#125;
</code></pre>
<h4>特定的 CA 证书如何配置？</h4>
<p>不论是权威机构颁发的证书还是自签名的，打包一份到 app 内部，比如存放在 asset 里，下面的示例展示了此过程：从 <strong>InputStream</strong> 获取一个特定的 CA，用该 CA 创建 <strong>KeyStore</strong>，然后用后者创建和初始化 <strong>TrustManager</strong>。TrustManager 是系统用于验证来自服务器的证书的工具，可以使用一个或多个 CA 从 <strong>KeyStore</strong>创建，而创建的 TrustManager 将仅信任这些 CA。</p>
<pre><code>    // Load CAs from an InputStream
    // (could be from a resource or ByteArrayInputStream or ...)
    CertificateFactory cf = CertificateFactory.getInstance("X.509");
    // From https://www.washington.edu/itconnect/security/ca/load-der.crt
    InputStream caInput = new BufferedInputStream(new FileInputStream("load-der.crt"));
    Certificate ca;
    try &#123;
        ca = cf.generateCertificate(caInput);
        System.out.println("ca=" + ((X509Certificate) ca).getSubjectDN());
    &#125; finally &#123;
        caInput.close();
    &#125;

    // Create a KeyStore containing our trusted CAs
    String keyStoreType = KeyStore.getDefaultType();
    KeyStore keyStore = KeyStore.getInstance(keyStoreType);
    keyStore.load(null, null);
    keyStore.setCertificateEntry("ca", ca);

    // Create a TrustManager that trusts the CAs in our KeyStore
    String tmfAlgorithm = TrustManagerFactory.getDefaultAlgorithm();
    TrustManagerFactory tmf = TrustManagerFactory.getInstance(tmfAlgorithm);
    tmf.init(keyStore);

    // Create an SSLContext that uses our TrustManager
    SSLContext context = SSLContext.getInstance("TLS");
    context.init(null, tmf.getTrustManagers(), null);
</code></pre>
<p>以上代码，可以解决证书信任问题。但同时需要注意的是，这里是基于Android默认的信任检查来解决的。因为我们没有对TrustManager做任何修改，如果仍然遇到证书校验不通过的情况，则需要重新实现TrustManager，请用以下代码代替“tmf.getTrustManagers()”：</p>
<p>。这时候我们需要通过自定义的校验方式方可完成校验。通过自定义<strong>X509TrustManager</strong>来实现checkServerTrusted的校验，其实就是通过上诉介绍的SSL/TLS校验的方式</p>
<pre><code>context.init(null, new TrustManager[]&#123;
          new X509TrustManager() &#123;
              @Override
              public void checkClientTrusted(X509Certificate[] chain,
                      String authType)
                      throws CertificateException &#123;
              &#125;

              @Override
              public void checkServerTrusted(X509Certificate[] chain,
                      String authType)
                      throws CertificateException &#123;
                  for (X509Certificate cert : chain) &#123;

                      // Make sure that it hasn't expired.
                      cert.checkValidity();

                      // Verify the certificate's public key chain.
                      try &#123;
                          cert.verify(((X509Certificate) ca).getPublicKey());
                      &#125; catch (NoSuchAlgorithmException e) &#123;
                          e.printStackTrace();
                      &#125; catch (InvalidKeyException e) &#123;
                          e.printStackTrace();
                      &#125; catch (NoSuchProviderException e) &#123;
                          e.printStackTrace();
                      &#125; catch (SignatureException e) &#123;
                          e.printStackTrace();
                      &#125;
                  &#125;
              &#125;

              @Override
              public X509Certificate[] getAcceptedIssuers() &#123;
                  return new X509Certificate[0];
              &#125;
          &#125;
  &#125;, null);
</code></pre>
<p>先校验证书的日期是否过期，其次通过本地预置证书的公钥对服务器下发的数字证书进行对比校验。</p>
<h4>如何通过文件配置证书？</h4>
<p>Android P新特性，全面禁止了非安全的http连接，如果要使用非加密连接，需要配置network security config</p>
<p>步骤如下：</p>
<ul>
<li>在res/xml下建立我们自己的network security config文件，名字任意，可以叫做network_security_config.xml</li>
<li>如果我们相对某些网址使用非安全连接，可以使用如下配置，以下可以说涵盖了很多配置。</li>
</ul>
<pre><code><?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    //用于辅助抓包，7.0以上证书的权限变了
    <base-config cleartextTrafficPermitted="true">
        <trust-anchors>
            //信任用户证书
            <certificates src="user"></certificates>

            //信任用户自己安装的证书
            <certificates src="system"></certificates>

            //定义白名单
            <certificates src="@raw/cn_area"></certificates>
        </trust-anchors>
    </base-config>

<!--    使用自签名 SSL 证书的主机 配置-->
<!--    cleartextTrafficPermitted="false" 强制校验https 否则可以允许通过http-->
    <domain-config cleartextTrafficPermitted="false">
        <domain includeSubdomains="true">example.com</domain>  <!-- 过滤域名，可配置多个 -->
        <domain includeSubdomains="true">example1.com</domain>  <!-- 一般会将 CDN 配置在此 -->
        <trust-anchors>
            <!--这就是我们自己的证书-->
            <!--如果要信任多个证书，就可以写多个-->
            <certificates src="@raw/cn_area"/>
            <!--也可以把这些证书放在一个目录下-->
            <certificates src="@raw/cn_area"/>

            //信任用户证书
            <certificates src="user"></certificates>

            //信任用户自己安装的证书
            <certificates src="system"></certificates>

        </trust-anchors>
<!--        固定证书-->
        <pin-set expiration="2018-01-01">
            <pin digest="SHA-256">7HIpactkIAq2Y49orFOOQKurWxmmSFZhBCoQYcRhJ3Y=</pin>
            <!-- backup pin -->
            <pin digest="SHA-256">fwza0LRMXouZHRC8Ei+4PyuldPDcf3UKgO/04cDM1oE=</pin>
        </pin-set>

    </domain-config>

<!--    debug 模式配置调试CA-->
    <debug-overrides>
        <trust-anchors>
            //信任用户证书
            <certificates src="user"></certificates>

            //信任用户自己安装的证书
            <certificates src="system"></certificates>
        </trust-anchors>
    </debug-overrides>

</network-security-config>

</code></pre>
<h5>下面方式可以通过具体的需求进行具体的配置</h5>
<p>如果我们的某个网址的证书是自签名的证书，我们想要访问这个网址，可以进行如下配置</p>
<pre><code><?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config>
        <domain includeSubdomains="true">example.com</domain>
        <trust-anchors>
            <!--这就是我们自己的证书-->
            <!--如果要信任多个证书，就可以写多个-->
            <certificates src="@raw/my_ca"/>
            <!--也可以把这些证书放在一个目录下-->
            <certificates src="@raw/trusted_roots"/>
        </trust-anchors>
    </domain-config>
</network-security-config>

</code></pre>
<p>如果我们想让App信任除系统之外的其他的CA，可以进行如下配置</p>
<pre><code><?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config>
        <trust-anchors>
          <!--在base-config中配置额外的CA-->
            <certificates src="@raw/extracas"/>
            <certificates src="system"/>
        </trust-anchors>
    </base-config>
</network-security-config>
</code></pre>
<p>如果我们在调试的时候staging服务器不是正规CA,我们可以进行如下配置</p>
<pre><code><?xml version="1.0" encoding="utf-8"?>
<network-security-config>
  <!--debug-overrides表示在调试状态下信任的CA,当android:debugable为true的时候，是调试状态-->
    <debug-overrides>
        <trust-anchors>
            <certificates src="@raw/debug_cas"/>
        </trust-anchors>
    </debug-overrides>
</network-security-config>
</code></pre>
<p>一般情况下，应用信任所有预装 CA。如果有预装 CA 签发欺诈性证书，则应用将面临被中间人攻击的风险。有些应用通过限制信任的 CA 集或通过固定证书，选择限制其接受的证书集</p>
<pre><code>    <?xml version="1.0" encoding="utf-8"?>
    <network-security-config>
        <domain-config>
            <domain includeSubdomains="true">example.com</domain>
            <pin-set expiration="2018-01-01">
                <pin digest="SHA-256">7HIpactkIAq2Y49orFOOQKurWxmmSFZhBCoQYcRhJ3Y=</pin>
                <!-- backup pin -->
                <pin digest="SHA-256">fwza0LRMXouZHRC8Ei+4PyuldPDcf3UKgO/04cDM1oE=</pin>
            </pin-set>
        </domain-config>
    </network-security-config>
</code></pre>
<p>更详细的信息请参考<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.android.com%2Ftraining%2Farticles%2Fsecurity-config" target="_blank">Android Security Config</a></p>
<p>数字证书转化<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2Fxiangguiwang%2Farticle%2Fdetails%2F76400805" target="_blank">https://blog.csdn.net/xiangguiwang/article/details/76400805</a></p>
  
</div>
            