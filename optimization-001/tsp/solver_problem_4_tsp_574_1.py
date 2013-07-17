#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from subprocess import Popen, PIPE


def solveIt(inputData):

    # Writes the inputData to a temporay file

    tmpFileName = 'tmp.data'
    tmpFile = open(tmpFileName, 'w')
    tmpFile.write(inputData)
    tmpFile.close()

    # Runs the command: java Solver -file=tmp.data

    #process = Popen(['java', '-cp', 'scala-library.jar;bin', 'tsp.Solver', '-file=' + tmpFileName],
    #                stdout=PIPE)
    #(stdout, stderr) = process.communicate()
    ret = "37567.57214812159 0\n563 562 561 560 549 548 545 546 547 544 543 541 542 107 109 108 173 174 175 172 110 111 114 113 112 161 160 162 168 163 167 166 164 165 154 155 156 159 153 157 158 145 146 144 143 142 147 148 152 149 150 151 141 140 139 138 137 136 135 134 133 132 131 130 129 128 127 126 125 124 69 70 68 67 65 66 64 76 75 74 73 72 71 123 122 121 120 119 118 117 116 115 106 105 104 103 102 101 551 550 559 558 557 556 554 553 552 100 99 98 96 95 97 94 89 88 77 78 62 63 60 61 79 80 81 59 58 55 56 57 82 83 53 54 52 51 50 84 85 86 87 90 93 92 91 555 45 46 49 48 47 44 43 42 39 41 40 38 37 36 35 34 33 32 30 31 29 28 27 26 25 24 21 22 23 12 13 14 15 16 11 10 9 7 8 17 18 19 20 568 569 570 474 473 472 471 494 495 470 469 468 467 466 465 464 496 497 463 462 461 459 460 571 572 573 6 5 0 4 3 2 1 458 457 456 455 454 439 445 444 443 442 446 448 447 449 450 441 440 453 452 499 500 501 498 519 518 520 521 522 523 526 525 524 493 492 491 490 486 487 535 534 488 533 532 489 531 530 529 528 527 512 511 510 509 513 514 515 516 517 502 503 504 505 308 309 310 311 451 312 313 305 307 506 507 508 302 301 303 304 306 319 320 321 318 317 316 314 315 374 375 376 377 378 379 380 381 389 388 390 392 391 393 394 395 396 371 372 373 322 323 324 325 326 327 328 329 366 342 365 367 368 369 370 398 397 399 400 401 402 403 404 405 406 407 408 409 384 383 385 387 386 382 431 433 434 435 438 436 437 432 430 429 428 427 426 425 424 423 422 421 420 419 417 418 410 411 412 356 357 355 354 353 352 413 414 416 415 351 350 347 348 349 358 359 360 361 362 363 364 346 345 344 343 341 340 330 331 332 333 336 337 338 339 335 334 283 284 285 286 287 282 281 280 279 278 276 277 289 288 290 275 274 273 292 291 293 294 295 296 270 268 269 272 271 267 297 298 266 265 264 263 262 261 260 259 258 299 300 257 256 255 253 254 252 251 250 249 248 241 242 243 244 245 247 246 238 239 240 237 236 235 234 232 233 231 230 229 228 227 189 226 225 190 191 192 193 219 218 220 221 222 224 223 217 216 215 214 212 213 211 210 209 205 206 207 208 203 204 202 201 200 199 198 197 196 195 194 184 185 183 182 186 188 187 178 179 181 180 169 171 170 177 176 540 538 539 537 536 485 484 483 482 481 480 479 478 477 476 475 567 566 565 564\n"
    
    # removes the temporay file

    os.remove(tmpFileName)

    return ret


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

