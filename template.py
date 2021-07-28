template = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="320" height="445" aria-labelledby="cardTitle" role="img">
  <title id="cardTitle">Now playing on Spotify</title>
  <foreignObject width="320" height="445">
    <style>
      div {
        font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji;
      }

      .container {
        background-color: #121212;
        border-radius: 10px;

        padding: 10px 10px
      }

      .playing {
        display: flex;
        justify-content: center;
        align-items: center;

        color: #53b14f;
        font-weight: bold;
        text-align: center;

        margin-bottom: 8px;
      }

      .not-play {
        color: #ff1616;
        text-align: center;

        margin-bottom: 0;
      }

      .artist {
        color: #fff;
        font-weight: bold;
        font-size: 20px;
        text-align: center;

        margin-bottom: 5px;
      }

      .song {
        color: #b3b3b3;
        font-size: 16px;
        text-align: center;

        margin-bottom: 22px;
      }

      .logo {
        margin-left: 5px;
      }

      .cover {
        border-radius: 5px;
      }

      #bars {
        height: 30px;
        margin: -30px 0 0 0px;
        position: absolute;
        width: 40px;
      }

      .bar {
        background: #53b14f;
        bottom: 1px;
        height: 3px;
        position: absolute;
        width: 3px;
        animation: sound 0ms -800ms linear infinite alternate;
      }

      @keyframes sound {
        0% {
          opacity: .35;
          height: 3px;
        }

        100% {
          opacity: 1;
          height: 22px;
        }
      }

      .bar:nth-child(1)  { left: 1px; animation-duration: 455ms; }.bar:nth-child(2)  { left: 5px; animation-duration: 445ms; }.bar:nth-child(3)  { left: 9px; animation-duration: 387ms; }.bar:nth-child(4)  { left: 13px; animation-duration: 464ms; }.bar:nth-child(5)  { left: 17px; animation-duration: 435ms; }.bar:nth-child(6)  { left: 21px; animation-duration: 469ms; }.bar:nth-child(7)  { left: 25px; animation-duration: 380ms; }.bar:nth-child(8)  { left: 29px; animation-duration: 413ms; }.bar:nth-child(9)  { left: 33px; animation-duration: 425ms; }.bar:nth-child(10)  { left: 37px; animation-duration: 440ms; }.bar:nth-child(11)  { left: 41px; animation-duration: 413ms; }.bar:nth-child(12)  { left: 45px; animation-duration: 491ms; }.bar:nth-child(13)  { left: 49px; animation-duration: 379ms; }.bar:nth-child(14)  { left: 53px; animation-duration: 397ms; }.bar:nth-child(15)  { left: 57px; animation-duration: 379ms; }.bar:nth-child(16)  { left: 61px; animation-duration: 481ms; }.bar:nth-child(17)  { left: 65px; animation-duration: 442ms; }.bar:nth-child(18)  { left: 69px; animation-duration: 427ms; }.bar:nth-child(19)  { left: 73px; animation-duration: 404ms; }.bar:nth-child(20)  { left: 77px; animation-duration: 445ms; }.bar:nth-child(21)  { left: 81px; animation-duration: 384ms; }.bar:nth-child(22)  { left: 85px; animation-duration: 402ms; }.bar:nth-child(23)  { left: 89px; animation-duration: 376ms; }.bar:nth-child(24)  { left: 93px; animation-duration: 497ms; }.bar:nth-child(25)  { left: 97px; animation-duration: 356ms; }.bar:nth-child(26)  { left: 101px; animation-duration: 474ms; }.bar:nth-child(27)  { left: 105px; animation-duration: 379ms; }.bar:nth-child(28)  { left: 109px; animation-duration: 490ms; }.bar:nth-child(29)  { left: 113px; animation-duration: 392ms; }.bar:nth-child(30)  { left: 117px; animation-duration: 424ms; }.bar:nth-child(31)  { left: 121px; animation-duration: 430ms; }.bar:nth-child(32)  { left: 125px; animation-duration: 488ms; }.bar:nth-child(33)  { left: 129px; animation-duration: 457ms; }.bar:nth-child(34)  { left: 133px; animation-duration: 386ms; }.bar:nth-child(35)  { left: 137px; animation-duration: 492ms; }.bar:nth-child(36)  { left: 141px; animation-duration: 444ms; }.bar:nth-child(37)  { left: 145px; animation-duration: 386ms; }.bar:nth-child(38)  { left: 149px; animation-duration: 374ms; }.bar:nth-child(39)  { left: 153px; animation-duration: 467ms; }.bar:nth-child(40)  { left: 157px; animation-duration: 480ms; }.bar:nth-child(41)  { left: 161px; animation-duration: 426ms; }.bar:nth-child(42)  { left: 165px; animation-duration: 400ms; }.bar:nth-child(43)  { left: 169px; animation-duration: 441ms; }.bar:nth-child(44)  { left: 173px; animation-duration: 480ms; }.bar:nth-child(45)  { left: 177px; animation-duration: 424ms; }.bar:nth-child(46)  { left: 181px; animation-duration: 485ms; }.bar:nth-child(47)  { left: 185px; animation-duration: 425ms; }.bar:nth-child(48)  { left: 189px; animation-duration: 498ms; }.bar:nth-child(49)  { left: 193px; animation-duration: 380ms; }.bar:nth-child(50)  { left: 197px; animation-duration: 366ms; }.bar:nth-child(51)  { left: 201px; animation-duration: 415ms; }.bar:nth-child(52)  { left: 205px; animation-duration: 480ms; }.bar:nth-child(53)  { left: 209px; animation-duration: 484ms; }.bar:nth-child(54)  { left: 213px; animation-duration: 391ms; }.bar:nth-child(55)  { left: 217px; animation-duration: 421ms; }.bar:nth-child(56)  { left: 221px; animation-duration: 431ms; }.bar:nth-child(57)  { left: 225px; animation-duration: 456ms; }.bar:nth-child(58)  { left: 229px; animation-duration: 435ms; }.bar:nth-child(59)  { left: 233px; animation-duration: 423ms; }.bar:nth-child(60)  { left: 237px; animation-duration: 417ms; }.bar:nth-child(61)  { left: 241px; animation-duration: 356ms; }.bar:nth-child(62)  { left: 245px; animation-duration: 457ms; }.bar:nth-child(63)  { left: 249px; animation-duration: 352ms; }.bar:nth-child(64)  { left: 253px; animation-duration: 423ms; }.bar:nth-child(65)  { left: 257px; animation-duration: 487ms; }.bar:nth-child(66)  { left: 261px; animation-duration: 391ms; }.bar:nth-child(67)  { left: 265px; animation-duration: 449ms; }.bar:nth-child(68)  { left: 269px; animation-duration: 477ms; }.bar:nth-child(69)  { left: 273px; animation-duration: 395ms; }.bar:nth-child(70)  { left: 277px; animation-duration: 381ms; }.bar:nth-child(71)  { left: 281px; animation-duration: 375ms; }.bar:nth-child(72)  { left: 285px; animation-duration: 440ms; }.bar:nth-child(73)  { left: 289px; animation-duration: 466ms; }.bar:nth-child(74)  { left: 293px; animation-duration: 440ms; }.bar:nth-child(75)  { left: 297px; animation-duration: 445ms; }
    </style>
    <div xmlns="http://www.w3.org/1999/xhtml" class="container">

        <div class="playing">Recently played on <img class="logo" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAE5ElEQVRYR81WS08bVxQ+dzweY48fQCCBllJDmqpRSx6gKizSiAUbILZjA21KVEhF20hNlLb/IKu2m3QRKaqQogIRkAXhYQxFSJGCQqVKrVSBQtpCFqEQkrQhxnb8Yjxzp7oTmdjjsWd4LHIlLzz3PL57zvedexG8Qgu9Qlhg22Bqumr0+/L2VdAMOpBvtdgCoedBnhPvsw/YpcFLg9x2DrklMA19DVajkf4B0dQnAMDkSJgQedwfWot9fevcraBWYJrA1HXX5RUWWG8jhGq1Bk7aiVj8PfGfWOc754uq+aqCOXXT8bFOTw2oBVLb5zmhw9s6fj2XXU4wniFnF6LRF2qJtO6LPPQMN3s/zWafFcxuA0kCwILYO+IZO6sESBHMbrUmWwVwQjw70jLWK9/PAEPIuqfQFtNa+u3acU8wKyd1BhjPqPNXJdVgHkP8WRwiqxGI/RsDLsSBiEXQGXRgKDCAqcQk/RgbA4hS1QXx/WPYPVaTepg0LzJHTBZmcy5wQQ5mL89CeCUMIGqvAQFjLjeD/aQdiqqLsoKLh/nCiTMT68nIaWA8Q45riKY6k5szF2YgEU5oR5HFkn2dhUNfHQLjXmOaBRZw34jHRwaotNLANHtdG6mTdaF3AVZvrwJCCNgyFoqOFIHtgA2MxUbQGXXSdyxg4MM8RJ9EYf2vdfDf80PsaUyxkqSNtd+nzU1+yOXVZ4Ahd429pCzjTiG80MIBeVH4GA/Lk8uw/PMyEL4lV9XFKiiuLt78H/2Hy5u8OEmK8LIyjb2Nbxvz9Qu5eiIKokTcuD8OfISXTk+zNOQV5r0grk6ZuIGFAMxdnpMIf+LHE0Dpqc00XCT+nq9t6l4aGOeNpia9iR6XgyHKuXv1rjYSI5BaWN5QDqUflAJFv0ya7ZBCHLeMfuQbSgPTPnG6LcLH+uVOM+dnIBFRIHGyCDlURgh7+JvDYCo1ZS04qzd3Xm/s/0lTZQJ/B2BxYBHK6sug+Ggx6M16Ge1BahdRHSHvytQKhB6E0pITMLXfKV/4QgK3jLbIKqOFM1vROFHW/NX5zdFw7NtjwL7GZoSIB/mqifaJ+bTKtF5qZfBRTmK14hIBuOccRB5GIPIoAhv+DeDjPDBWBsxvmMFaaQVDviGjaut/rkNgMQAVpyoUwyqqiVg2e11E2pu6l7xFgDtf3gEiVS2LgNv/4X4oPV6qxVx5zhBPz5CjG9FU2vUuiiJMd05LcrRWWKHg3QKwvGkBJv/FHUQkHl4Ow9rsGhAJp86USncl2F32rKCwgG+MeHxtSYO0wVDfVW+zlbABLUfKLlUBFvsW4fEvjyWTg50HJZkrrfDT+J6pz6b8imCk6ow4f0MUen8ngKTuCiIsjS+B3WFXnOAiFueG3WNHUvNkjExHl8PElFCRnYJR83/2MGiZPj8dzgmGbLoGT7bTjC7jJaaWQOs+zwmfe1vHr8ntc7yBXd2IBsW3qtakSnYixgPDbt8Zpb2cTzL3sLOH0qGOnSRP9c0FhNipvg/dN5s6KD3ds1NA2Vqjyhl5YkJq/V40gyhUvVVQRDX+R6HjcrJuuU1yh6b+pgLGSF2hdNRpAKBzAOOxgAejfu5C6hxRO4hqm7IFaLjSYKCL8Fs6HfOO1WK1haKhYCKKF3AA30++3NSSa1bTVgPthv22K7MbyeUx/gfIiuIzZiZJFQAAAABJRU5ErkJggg==" />
        </div>
        <div class="artist">@ARTIST</div>
        <div class="song">@SONG</div>
        <div id="bars"></div>


          <a href="{}" target="_BLANK">
            <center>
              <img src="@IMAGE" width="300" height="300" class="cover" />
            </center>
          </a>




    </div>
  </foreignObject>
</svg>"""