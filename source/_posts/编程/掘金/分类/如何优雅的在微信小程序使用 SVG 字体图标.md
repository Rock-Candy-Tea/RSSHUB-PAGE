
---
title: '如何优雅的在微信小程序使用 SVG 字体图标'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16cfaf7b06054a389ca1d4112c62c78c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 06:57:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16cfaf7b06054a389ca1d4112c62c78c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:18px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:40px;margin-bottom:20px;color:#007fff;display:flex;align-items:center&#125;.markdown-body h1:hover:before,.markdown-body h2:hover:before,.markdown-body h3:hover:before,.markdown-body h4:hover:before,.markdown-body h5:hover:before,.markdown-body h6:hover:before&#123;transition:All .4s ease-in-out;transform:rotate(1turn)&#125;.markdown-body h1&#123;font-size:30px;background:linear-gradient(#fff 60%,#c6e3ff 0)&#125;.markdown-body h1:before&#123;content:"";display:inline-block;width:32px;height:32px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h2&#123;font-size:24px;background:linear-gradient(#fff 60%,#cce3fb 0)&#125;.markdown-body h2:before&#123;content:"";display:inline-block;width:24px;height:24px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3:before&#123;content:"";display:inline-block;width:18px;height:18px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h4&#123;font-size:18px&#125;.markdown-body h4:before&#123;content:"";display:inline-block;width:16px;height:16px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h5:before&#123;content:"";display:inline-block;width:15px;height:15px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h6&#123;font-size:14px&#125;.markdown-body h6:before&#123;content:"";display:inline-block;width:12px;height:12px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;border-bottom:2px solid #007fff;color:#007fff;padding-right:10px&#125;.markdown-body p&#123;letter-spacing:1px;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:10px auto&#125;.markdown-body hr&#123;border:none;border-top:1px dashed #92c8ff&#125;.markdown-body hr:before&#123;content:"✂";display:inline-block;position:relative;top:-12px;left:40px;padding:0 3px;color:#007fff;font-size:18px&#125;.markdown-body hr:after&#123;content:"按虚线剪开";position:relative;top:-15px;left:84%;padding:0 3px;color:#007fff;font-size:12px&#125;.markdown-body del&#123;color:#f44&#125;.markdown-body em&#123;color:#007fff;margin:0 2px&#125;.markdown-body strong&#123;color:#007fff;font-weight:bolder&#125;.markdown-body code&#123;word-break:break-word;border-radius:4px;overflow-x:auto;background-color:#e6f3ff;color:#007fff;font-weight:600;font-size:16px;padding:.065em .4em;border:1px solid #007fff&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:5px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:18px;font-weight:400;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8;border:none&#125;.markdown-body a&#123;text-decoration:none;color:#007fff;border-bottom:1px solid #007fff&#125;.markdown-body a:before&#123;content:"¶";margin-right:5px;font-size:22px&#125;.markdown-body a:after&#123;content:"↷";margin-left:2px;font-size:22px;display:none&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c;border-bottom:1px solid #275b8c&#125;.markdown-body a:active:after,.markdown-body a:hover:after&#123;display:inline-block&#125;.markdown-body table&#123;display:inline-block!important;font-size:16px;width:auto;max-width:100%;overflow:auto;border:1px solid #a5d3ff&#125;.markdown-body thead&#123;background:#c6e3ff;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#eef7ff&#125;.markdown-body tbody>tr:nth-child(odd)&#123;background-color:#f8fcff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #007fff;background-color:#eef7ff&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#007fff&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
</blockquote>
<blockquote>
<p>本文思路来自实际项目的重构总结，欢迎纠正和交流。如果对你有帮助，还请点赞👍收藏支持一下啦。</p>
</blockquote>
<p>最近在重构一个项目，主要是做 H5 端和小程序端，这次打算开始多做总结啦，之前已经总结一篇<a href="https://juejin.cn/post/6986455896708612110" target="_blank" title="https://juejin.cn/post/6986455896708612110">《如何优雅的管理 HTTP 请求和响应拦截器？》</a> 。</p>
<p>如果大家还有其他方案，欢迎一起探讨哈~ 喜欢本文的朋友给个赞👍鼓励一下哈~</p>
<h2 data-id="heading-0">一、需求思考和方案设计</h2>
<p>本文介绍的项目是使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2FREADME" target="_blank" rel="nofollow noopener noreferrer" title="https://taro-docs.jd.com/taro/docs/README" ref="nofollow noopener noreferrer">Taro</a>框架进行多端开发，目前主要适配 H5 端和微信小程序端。项目使用的字体图标库内部维护，目前托管在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iconfont.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iconfont.cn/" ref="nofollow noopener noreferrer">iconfont</a> 上。</p>
<h3 data-id="heading-1">1. 问题分析</h3>
<p>最近在重构的项目比较古老（其实也就去年的），项目中使用到的图标早已更新 N 个迭代了，已经由<strong>单色图标</strong>更新到<strong>多色图标</strong>！
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16cfaf7b06054a389ca1d4112c62c78c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
很明显好看多了。</p>
<p>这里先按照 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iconfont.cn%2Fhelp%2Fdetail%3Fspm%3Da313x.7781069.1998910419.d8cf4382a%26helptype%3Dcode" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iconfont.cn/help/detail?spm=a313x.7781069.1998910419.d8cf4382a&helptype=code" ref="nofollow noopener noreferrer">iconfont 的规则</a>看看单色图标和多色图标使用上的区别：</p>
<h4 data-id="heading-2">单色图标的使用</h4>
<p>单色图标使用起来比较简单（以 font-class 引用为例），只需要 2 个步骤：</p>
<ul>
<li>第一步：拷贝项目下面生成的fontclass代码：</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css">//at<span class="hljs-selector-class">.alicdn</span><span class="hljs-selector-class">.com</span>/t/font_8d5l8fzk5b87iudi<span class="hljs-selector-class">.css</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二步：挑选相应图标并获取类名，应用于页面：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"iconfont icon-xxx"</span>></span><span class="hljs-tag"></<span class="hljs-name">i</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">多色图标的使用</h4>
<p>多色图标使用起来也很简单（以 symbol 引用为例），只需要 3 个步骤：</p>
<ul>
<li>第一步：拷贝项目下面生成的symbol代码：</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">//at.alicdn.com/t/font_8d5l8fzk5b87iudi.js
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二步：加入通用css代码（引入一次就行）：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
    <span class="hljs-selector-class">.icon</span> &#123;
       <span class="hljs-attribute">width</span>: <span class="hljs-number">1em</span>; <span class="hljs-attribute">height</span>: <span class="hljs-number">1em</span>;
       <span class="hljs-attribute">vertical-align</span>: -<span class="hljs-number">0.15em</span>;
       fill: currentColor;
       <span class="hljs-attribute">overflow</span>: hidden;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第三步：挑选相应图标并获取类名，应用于页面：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"icon"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"#icon-xxx"</span>></span><span class="hljs-tag"></<span class="hljs-name">use</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两种图标在使用上都非常方便，那大家是不是会好奇，我们写本文的目的？</p>
<p>原因是，<strong>微信小程序上不支持 SVG 字体图标！😔 而多色图标，是需要借助 SVG 标签来实现。</strong></p>
<p>于是我在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fcomponent%2Fimage.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/component/image.html" ref="nofollow noopener noreferrer">小程序文档</a>找了好久，也只看到了 <code><Image></code> 组件能够使用 SVG，介绍如下：</p>
<blockquote>
<p>image图片。支持 JPG、PNG、SVG、WEBP、GIF 等格式，2.3.0 起支持云文件ID。</p>
</blockquote>
<p>其属性 <code>src</code> 的值为图片资源地址，这就意味着，不能使用 SVG 字体图标了。因此我们需要想想变通的办法。</p>
<p>（这里不讨论将 iconfont 上图标下载为图片来引用的情况）</p>
<h3 data-id="heading-4">2. 方案设计</h3>
<p>既然我们了解了单色图标和多色图标的使用方式：</p>
<ul>
<li>单色图标：任意标签（如 <code>div</code> 标签） + 对应字体图标 class 名称</li>
<li>多色图标：使用 <code>svg</code> 标签 + <code>use</code> 标签设置 <code>xlink:href</code> 属性</li>
</ul>
<p>首先马上想到的是，能不能集合两者使用方式，实现任意标签通过 class 名称来使用多色图标？</p>
<p>答案是可以的，只需要对图标文件进行格式转换，即 <strong>将多色字体图标转换为能通过class名称来引用的字体图标文件</strong> 。</p>
<p>那接下来只要看看如何实现格式转换即可。</p>
<h2 data-id="heading-5">二、重构后的效果</h2>
<p>这边我以其中一个页面进行重构，最后将单色图标全都换成新的多色 SVG 字体图标，效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c102f716f07a4c489bac801c9ed71ebe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">三、方案一：手动转换图标文件</h2>
<p>目前我尝试了两套方案，并且都顺利实现效果，这边先分享一下这两种方案，然后再补充说明我选择哪个方案和原因：</p>
<p>该方案实现的是手动将字体图标库文件转换成能通过 class 名称来引用的图标库。
使用到的工具有：</p>
<ol>
<li>icomoon：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ficomoon.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://icomoon.io/" ref="nofollow noopener noreferrer">icomoon.io/</a> 用来打包图标。</li>
<li>transfonter： <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftransfonter.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://transfonter.org/" ref="nofollow noopener noreferrer">transfonter.org/</a> 用来生成 base64 格式的图标。</li>
</ol>
<p>接下来开始试试：</p>
<h3 data-id="heading-7">步骤一：通过 iconfont 下载需要的 SVG 格式的图标</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2f2ed0981774d3082f29812b7226cc8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这边多下载了几个，都是 svg 格式的文件，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61210334a3d148f4ac06c3b24c071663~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">步骤二：打包字体图标</h3>
<p>这一步是将零散个多个 SVG 多色图标打包成一个字体图标文件，这一步需要使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ficomoon.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://icomoon.io/" ref="nofollow noopener noreferrer">icomoon.io/</a>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0758d7a86d8046d99e0d3293c3ac44ba~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e710ef82d7b445b8503eeddd3616a4d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac14cf323a0a4c30896528abd519e04a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49d1b72417614cb4847b42d8a51c8b83~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">步骤三：字体图标进行 Base64 编码</h3>
<p>接下来就需要将打好的字体图标进行 base64 压缩，这边使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftransfonter.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://transfonter.org/" ref="nofollow noopener noreferrer">transfonter.org/</a>来操作。</p>
<p>第一步选择前面打好的包里面的 <code>.ttf</code> 文件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52c375c7a20a4dcdb45b9b9b6aa76fe7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置参数，并导出文件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b074d244eafd4efbb33ec0a339c7e41a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">步骤四：合并字体图标</h3>
<p>经过前面几个步骤，我们现在已经有 2 个包：</p>
<ul>
<li>第一个包：icomoon 生成的包</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d8be45c189442f8bfa18d33c9325b0b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>第二个包：transfonter 生成的包</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f8f7d9414aa4e43b8ad21dd44747c64~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们开始将两个包合并：
将第一个包 style.css 文件除 <code>@font-face</code> 的内容复制到第二个包 stylesheet.css 文件后面。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47f9996d991a4a7bb8af9a7fd84e8a23~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就获得一份新的字体图标文件，其实也可以拷贝到一份新的 css 文件中。</p>
<h3 data-id="heading-11">使用字体图标</h3>
<p>我们将前面修改后的文件改名为 <code>icon.scss</code> 并引入到项目：</p>
<pre><code class="hljs language-css copyable" lang="css">// app<span class="hljs-selector-class">.scss</span>

<span class="hljs-keyword">@import</span> <span class="hljs-string">"./style/icon.scss"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中使用图标：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><View className=<span class="hljs-string">"icon-exe-knowledge-ppt"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path1'</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path2'</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path3'</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path4'</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path5'</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path6'</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
</View>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c48ca101e0d8458c970eaceb562c641c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">踩坑记录</h3>
<p>在使用方案一的时候，踩了好几个坑，这边挑两个来说：</p>
<ul>
<li>使用时，需要手动添加几个 <code><View classname="path*"></View></code> 元素</li>
</ul>
<p>刚开始使用，图标一直没有出来，后面观察字体图标，它是在容器元素下很多个 <code>path1</code> 、 <code>path2</code> 等元素的伪类中去渲染图标内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35107552afc042f388757059de967143~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以使用时需要手动添加一下。</p>
<ul>
<li>默认图标会是一个大的块级元素，导致图标显示有问题</li>
</ul>
<p>这是因为手动加的 class 为 <code>path*</code> 的 <code>View</code> 标签本身是块级元素，所以这里只要简单加个 <code>display: flex</code> 即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f6cf5d1753b4221af6614ce964683cc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>并且其字体大小，也是可以使用 <code>font-size</code> 来设置：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">display</span>: flex;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">100px</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">抽取组件</h3>
<p>考虑到复用性，我将这些抽成一个 <code>exe-svg-icon</code> 组件：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> Taro <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/taro'</span>;
<span class="hljs-keyword">import</span> &#123; View, Text &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/components'</span>;
<span class="hljs-keyword">import</span> classNames <span class="hljs-keyword">from</span> <span class="hljs-string">'classnames'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">EXESvgIcon</span>(<span class="hljs-params">params</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; icon = <span class="hljs-string">'exe-none'</span> &#125; = params;
  <span class="hljs-keyword">const</span> containerStyle = &#123;
    <span class="hljs-attr">display</span>: <span class="hljs-string">'inline-block'</span>
  &#125;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;classNames(</span>'<span class="hljs-attr">svg</span>', <span class="hljs-attr">icon</span>)&#125; <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path1'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path2'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path3'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      &#123;/* 一般图标 3 层，这边多预留几层，防止不够用 */&#125;
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path4'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path5'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path6'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path7'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path8'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'path9'</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;containerStyle&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">View</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  )
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> EXESvgIcon;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这边，方案一实现完成。</p>
<h2 data-id="heading-14">四、方案二：借助第三方库实现</h2>
<p>由于第一个方案使用起来比较繁琐，于是我又再研究其他简单点的方案。</p>
<p>直到我看到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fmirrors%2FTaro-Iconfont" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/mirrors/Taro-Iconfont" ref="nofollow noopener noreferrer">taro-iconfont-cli</a> 这个库。</p>
<blockquote>
<p>在Taro框架中使用iconfont图标，不依赖字体，支持多色彩。</p>
</blockquote>
<p>目前支持平台包括：</p>
<ul>
<li>微信小程序</li>
<li>支付宝小程序</li>
<li>百度小程序</li>
<li>头条小程序</li>
<li>QQ小程序</li>
<li>H5</li>
</ul>
<p>有以下特性：</p>
<ul>
<li>一键生成标准组件，多端支持</li>
<li>使用方便，import即可</li>
<li>支持多色彩</li>
<li>支持自定义颜色</li>
<li>支持 ES6 和 TypeScript 两种模式</li>
</ul>
<p>按照文档描述，只需要 3 个步骤，那么试试看：</p>
<h3 data-id="heading-15">步骤一：安装 taro-iconfont-cli</h3>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># Yarn</span>
yarn add taro-iconfont-cli --dev

<span class="hljs-comment"># Npm</span>
npm install taro-iconfont-cli --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，如果使用的是 Taro 2.x，请安装 <strong><code>**taro-iconfont-cli@2.1.0**</code></strong>，并阅读旧版的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ficonfont-cli%2Ftaro-iconfont-cli%2Fblob%2Fv2.1.0%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/iconfont-cli/taro-iconfont-cli/blob/v2.1.0/README.md" ref="nofollow noopener noreferrer">README.md</a>。</p>
<h3 data-id="heading-16">步骤二：生成配置文件</h3>
<p>通过命令生成 iconfont.json 配置文件：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx iconfont-init

<span class="hljs-comment"># 可传入配置输出路径</span>
<span class="hljs-comment"># npx iconfont-init --output iconfont.json</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时项目根目录会生成一个<code>iconfont.json</code>的文件，内容如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"symbol_url"</span>: <span class="hljs-string">"请参考README.md，复制 http://iconfont.cn 官网提供的JS链接"</span>,
  <span class="hljs-attr">"save_dir"</span>: <span class="hljs-string">"./src/components/iconfont"</span>,
  <span class="hljs-attr">"use_typescript"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"platforms"</span>: <span class="hljs-string">"*"</span>,
  <span class="hljs-attr">"use_rpx"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"trim_icon_prefix"</span>: <span class="hljs-string">"icon"</span>,
  <span class="hljs-attr">"default_icon_size"</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">"design_width"</span>: <span class="hljs-number">750</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>symbol_url</code> 值需要在 iconfont 中复制</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/246e746ed45d42afa5ae93a9b9cfe15b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">步骤三：生成 Taro 标准组件</h3>
<p>通过命令，生成 Taro 标准组件：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx iconfont-taro

<span class="hljs-comment"># 可传入配置文件路径</span>
<span class="hljs-comment"># npx iconfont-taro --config iconfont.json</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过控制台，我们可以看到 taro-iconfont-cli 为每个图标单独生成一个 Taro 组件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ba58b7294c240f58a83b26f3d5bd1b6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80ff739befa843469c5af0d0beeabec1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">使用字体图标</h3>
<p>按照文档使用方法，使用的时候，只需要引入 <code>IconFont</code> 组件，通过 <code>name</code> 名称来选择对应图标即可：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 省略其他代码</span>

<span class="hljs-keyword">import</span> IconFont <span class="hljs-keyword">from</span> <span class="hljs-string">'@components/Iconfont/index'</span>;

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">IconFont</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"exe-knowledge-ppt"</span>></span><span class="hljs-tag"></<span class="hljs-name">IconFont</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照文档提示，还有更多使用方法：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 原色彩</span>
<IconFont name=<span class="hljs-string">"alipay"</span> />

<span class="hljs-comment">// 单色：红色</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">IconFont</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"alipay"</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"red"</span> /></span></span>

<span class="hljs-comment">// 多色：红色+橘色</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">IconFont</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"alipay"</span> <span class="hljs-attr">color</span>=<span class="hljs-string">&#123;[</span>'<span class="hljs-attr">red</span>', '<span class="hljs-attr">orange</span>']&#125; <span class="hljs-attr">size</span>=<span class="hljs-string">&#123;300&#125;</span> /></span></span>

<span class="hljs-comment">// 不同格式的颜色写法</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">IconFont</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"alipay"</span> <span class="hljs-attr">color</span>=<span class="hljs-string">&#123;[</span>'#<span class="hljs-attr">333</span>', '<span class="hljs-attr">rgb</span>(<span class="hljs-attr">50</span>, <span class="hljs-attr">124</span>, <span class="hljs-attr">39</span>)']&#125; /></span></span>

<span class="hljs-comment">// 与文字对齐</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> '<span class="hljs-attr">flex</span>', <span class="hljs-attr">alignItems:</span> '<span class="hljs-attr">center</span>' &#125;&#125;></span>
  <span class="hljs-tag"><<span class="hljs-name">Text</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">IconFont</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"alipay"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">踩坑记录</h3>
<ol>
<li>字体大小设置问题</li>
</ol>
<p>由于通过这种方式导出的图标，是个单独组件，使用时如果需要设置图标大小，需要通过设置其 <code>width</code>和<code>height</code>属性进行设置。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2a1543852b9471faf58996659570723~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过 <code>font-size</code>属性无法设置字体图标的大小。</p>
<h2 data-id="heading-20">五、方案对比和选择</h2>
<p>这次只尝试了这两种方案，都能顺利完成需求。如果大家有其他方案，欢迎一起评论区讨论~</p>
<p>接下来<strong>以生成下面相同 20 个多色图标为标准，分析这两种方案：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f78d0a522394926a71c0243988ca945~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>先看看对比结果：</p>

























<table><thead><tr><th></th><th><strong>手动转换图标文件</strong></th><th><strong>借助 taro-iconfont-cli 库实现</strong></th></tr></thead><tbody><tr><td><strong>生成难易程度</strong></td><td>复杂</td><td>简单</td></tr><tr><td><strong>使用难易程度</strong></td><td>简单</td><td>简单</td></tr><tr><td><strong>资源占用程度</strong></td><td>27kb</td><td>420kb（项目未打包前）</td></tr></tbody></table>
<p>分析每个项目：</p>
<h3 data-id="heading-21">1. 对比生成难易程度</h3>
<ul>
<li>「手动转换图标文件」需要每次将图标单独下载，再进行打包，当图标数量较多，其工作量就较大。</li>
<li>「taro-iconfont-cli」只需设置字体图标库地址，自动下载并生成组件，较为方便。</li>
</ul>
<h3 data-id="heading-22">2. 对比使用难易程度</h3>
<p>两者使用起来都比较简单：</p>
<ul>
<li>「手动转换图标文件」为元素添加 class 名称即可。</li>
<li>「taro-iconfont-cli」为元素添加 name 属性。</li>
</ul>
<h3 data-id="heading-23">3. 对比资源占用情况</h3>
<p>资源占用差异就很大了，分析下原因：</p>
<ul>
<li>「手动转换图标文件」是将图标重新打包，最后生成的都是 base64 编码的内容，相对较小。</li>
<li>「taro-iconfont-cli」是为每个图标生成一个组件，单独一个文件，还有附加各个平台的文件，因此较大。</li>
</ul>
<h3 data-id="heading-24">4. 选择方案</h3>
<p>考虑到目前项目所使用的字体图标比较少（20 个以内），后续开发人员上手难度问题，我最终使用「taro-iconfont-cli」这套方案。
虽然这个方案生成的组件资源占用会稍大，但是目前使用图标较少，并且可以通过打包工具、CDN 等常用优化方式进行优化。</p>
<h2 data-id="heading-25">六、本文总结</h2>
<p>本文通过一次简单的项目重构，总结项目中小程序使用 SVG 多色图标的方案，目的是为了实现在小程序中能够正常使用 SVG 多色图标，并且也为内容越来越多独立站点的项目积累经验，毕竟各个项目具有相关性。</p>
<p>最后，「taro-iconfont-cli」方案目前已经在内部 npm 仓库维护，采用版本控制，方便不同项目使用时减少冲突。</p>
<p>当然，本文是基于我的经验总结，欢迎大家有更好的方案，一起讨论学习~~</p>
<h2 data-id="heading-26">参考文章</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FOriginally_M%2Farticle%2Fdetails%2F106473475" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/Originally_M/article/details/106473475" ref="nofollow noopener noreferrer">微信小程序中使用svg字体图标教程 ——图解三步，很清晰</a> </li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fmirrors%2FTaro-Iconfont" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/mirrors/Taro-Iconfont" ref="nofollow noopener noreferrer">Taro-Iconfont</a> </li>
</ul></div>  
</div>
            